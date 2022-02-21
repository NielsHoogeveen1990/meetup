import abc
from typing import TypeVar
from typing import List

from pydantic import BaseModel
PandasDataFrame = TypeVar("pandas.core.frame.DataFrame")


class PlotterBase(BaseModel):
    df: PandasDataFrame
    X_col: str
    y_cols: List[str]
    mode: str
    title: str
    export: bool
    auto_size: bool
    height: int = 400
    width: int = 800

    @abc.abstractmethod
    def show(self):
        pass