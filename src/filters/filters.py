import operator
from typing import List, Dict, Any

import pandas as pd

# Mapping of string comparison operators to callable functions
OPS = {
    ">": operator.gt,
    ">=": operator.ge,
    "<": operator.lt,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne,
}


def apply_filters_df(df: pd.DataFrame, filters: List[Dict[str, Any]]) -> pd.DataFrame:
    """Filter ``df`` using a list of column/operation/value dictionaries.

    Parameters
    ----------
    df:
        DataFrame to filter.
    filters:
        A list where each item has ``col``, ``op`` and ``val`` keys. ``op`` must
        be one of the operators defined in :data:`OPS`.

    Returns
    -------
    pd.DataFrame
        The filtered DataFrame.
    """
    df_filtered = df.copy()
    for f in filters:
        col = f.get("col")
        op = f.get("op")
        val = f.get("val")
        if col in df_filtered.columns and op in OPS:
            df_filtered = df_filtered[OPS[op](df_filtered[col], val)]
    return df_filtered


def interactive_filter(df: pd.DataFrame, columns_to_filter: List[str]) -> None:
    """Display interactive widgets to filter ``df`` inside a Jupyter notebook."""

    try:
        import ipywidgets as widgets
        from IPython.display import display, clear_output
    except ImportError as exc:  # pragma: no cover - optional dependency
        raise ImportError("ipywidgets is required for interactive filtering") from exc

    widgets_dict = {
        col: widgets.FloatRangeSlider(
            value=[float(df[col].min()), float(df[col].max())],
            min=float(df[col].min()),
            max=float(df[col].max()),
            step=1.0,
            description=col,
            continuous_update=False,
            layout=widgets.Layout(width="90%"),
        )
        for col in columns_to_filter
        if col in df.columns
    }

    button = widgets.Button(description="Aplicar Filtros")
    output = widgets.Output()

    def on_button_click(_):
        with output:
            clear_output()
            df_filtered = df.copy()
            for col, slider in widgets_dict.items():
                min_val, max_val = slider.value
                df_filtered = df_filtered[
                    (df_filtered[col] >= min_val) & (df_filtered[col] <= max_val)
                ]
            print(f"A\u00e7\u00f5es filtradas: {df_filtered.shape[0]}")
            display(df_filtered.head(10))

    button.on_click(on_button_click)
    display(*widgets_dict.values(), button, output)

