from datetime import datetime
from datetime import timedelta

from meetup.plotter.plot_base import PlotterBase
from typing import TypeVar
import plotly.graph_objects as go
PandasDataFrame = TypeVar("pandas.core.frame.DataFrame")


class ErrorPlotter(PlotterBase):

    def show(self, timedelta_minutes: int):
        errors = self.df.loc[lambda d: ~d['error'].isna()]['timestamp'].values

        # Create data traces
        data = []
        for col in self.y_cols:
            trace = go.Scatter(x=self.df[self.X_col],
                               y=self.df[col],
                               mode=self.mode,
                               name=col
                               )
            data.append(trace)

        if self.auto_size:
            # Create layout
            layout = go.Layout(title=self.title,
                               autosize=True
                               )
            # Create figure object
            fig = go.Figure(data=data, layout=layout)
            for error in errors:
                date_time_obj = datetime.strptime(error, '%Y-%m-%d %H:%M:%S')
                new_time = date_time_obj - timedelta(minutes=timedelta_minutes)

                fig.add_vline(x=error, line_width=3, line_dash="dash", line_color="red")

                fig.add_vrect(x0=str(new_time), x1=error,
                              annotation_text="anomaly", annotation_position="top left",
                              fillcolor="red", opacity=0.25, line_width=0)

            fig.update_layout(hovermode="x unified")
            # Display
            if self.export:
                fig.write_html('errors.html')

            elif self.export is False:
                fig.show()

        else:
            # Create layout
            layout = go.Layout(title=self.title,
                               autosize=False,
                               width=self.width,
                               height=self.height
                               )
            # Create figure object
            fig = go.Figure(data=data, layout=layout)
            for error in errors:
                date_time_obj = datetime.strptime(error, '%Y-%m-%d %H:%M:%S')
                new_time = date_time_obj - timedelta(minutes=timedelta_minutes)

                fig.add_vline(x=error, line_width=3, line_dash="dash", line_color="red")

                fig.add_vrect(x0=str(new_time), x1=error,
                              annotation_text="anomaly", annotation_position="top left",
                              fillcolor="red", opacity=0.25, line_width=0)

            fig.update_layout(hovermode="x unified")
            if self.export:
                fig.write_html('errors.html')

            elif self.export is False:
                fig.show()