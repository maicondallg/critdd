import pandas as pd
from critdd import Diagram

if __name__ == "__main__":
    filename = "teste.csv"
    df = pd.read_csv(filename, index_col=0)

    diagram = Diagram(
        -(df).to_numpy(),
        treatment_names=df.columns,
        maximize_outcome=True,
        adjustment=None,
        critical_difference="nemeyi",
    )
    diagram.to_file("plots/ExemploF1.png",
                    reverse_x=False,
                    adjustment=None,
                    )
