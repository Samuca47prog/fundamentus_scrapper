"""Simple Tkinter GUI for displaying stocks, applying filters and showing graphs."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import List, Dict, Any

import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from filters.filters import apply_filters_df, OPS


class StockApp(tk.Tk):
    """Main application window."""

    def __init__(self, df: pd.DataFrame) -> None:
        super().__init__()
        self.title("Fundamentus Stocks")
        self.geometry("1024x768")

        # ensure the application closes cleanly when the window is
        # dismissed via the window manager close button ("X")
        self.protocol("WM_DELETE_WINDOW", self._on_close)

        self.df_original = df
        self.df_filtered = df
        self.current_filters: List[Dict[str, Any]] = []

        self._create_frames()
        self._create_table()
        self._create_filter_controls()
        self._create_graph()
        self._populate_table(self.df_filtered)

    def _on_close(self) -> None:
        """Handle the window close event."""
        self.destroy()
        self.quit()
        plt.close(self.figure)

    def _create_frames(self) -> None:
        """Create layout frames for table, filters and graphs."""
        self.table_frame = ttk.Frame(self)
        self.filter_frame = ttk.Frame(self)
        self.graph_frame = ttk.Frame(self)

        self.table_frame.pack(side="top", fill="both", expand=True)
        self.filter_frame.pack(side="left", fill="y")
        self.graph_frame.pack(side="right", fill="both", expand=True)

    def _create_table(self) -> None:
        """Initialize table view."""
        columns = list(self.df_original.columns)
        self.tree = ttk.Treeview(
            self.table_frame, columns=columns, show="headings", height=15
        )
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=80)
        self.tree.pack(fill="both", expand=True)

    def _populate_table(self, df: pd.DataFrame) -> None:
        """Populate treeview with ``df`` contents."""
        self.tree.delete(*self.tree.get_children())
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

    def _create_filter_controls(self) -> None:
        """Create widgets used to build and apply filters."""
        cols = [
            c
            for c in self.df_original.columns
            if pd.api.types.is_numeric_dtype(self.df_original[c])
        ]
        ttk.Label(self.filter_frame, text="Column").pack(anchor="w")
        self.col_var = tk.StringVar()
        ttk.Combobox(self.filter_frame, textvariable=self.col_var, values=cols).pack(
            fill="x"
        )

        ttk.Label(self.filter_frame, text="Operator").pack(anchor="w")
        self.op_var = tk.StringVar()
        ttk.Combobox(
            self.filter_frame, textvariable=self.op_var, values=list(OPS.keys())
        ).pack(fill="x")

        ttk.Label(self.filter_frame, text="Value").pack(anchor="w")
        self.val_entry = ttk.Entry(self.filter_frame)
        self.val_entry.pack(fill="x")

        ttk.Button(
            self.filter_frame, text="Add Filter", command=self._add_filter
        ).pack(fill="x", pady=5)
        ttk.Button(
            self.filter_frame, text="Apply Filters", command=self._apply_filters
        ).pack(fill="x")

        self.filters_box = tk.Listbox(self.filter_frame, height=8)
        self.filters_box.pack(fill="both", expand=True, pady=(5, 0))

    def _create_graph(self) -> None:
        """Prepare matplotlib figure canvas."""
        self.figure, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def _add_filter(self) -> None:
        """Add filter definition to current list."""
        try:
            value = float(self.val_entry.get())
        except ValueError:
            return
        filt = {"col": self.col_var.get(), "op": self.op_var.get(), "val": value}
        if not filt["col"] or not filt["op"]:
            return
        self.current_filters.append(filt)
        self.filters_box.insert(tk.END, f"{filt['col']} {filt['op']} {filt['val']}")
        self.val_entry.delete(0, tk.END)

    def _apply_filters(self) -> None:
        """Filter DataFrame and refresh table and graph."""
        self.df_filtered = apply_filters_df(self.df_original, self.current_filters)
        self._populate_table(self.df_filtered)
        self._update_graph()

    def _update_graph(self) -> None:
        """Plot basic bar chart of filtered data count by column."""
        self.ax.clear()
        if not self.df_filtered.empty:
            self.df_filtered.count().plot.bar(ax=self.ax)
        self.canvas.draw()


def run(df: pd.DataFrame) -> None:
    """Launch the :class:`StockApp` with ``df``."""
    app = StockApp(df)
    app.mainloop()

