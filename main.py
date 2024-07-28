import sys

import pandas as pd
import numpy as np
from critdd import Diagram

if __name__ == "__main__":
    filename = "ExemploF1.csv"
    df = pd.read_csv(filename, index_col=0)

    diagram = Diagram(
        df.to_numpy(),
        treatment_names=df.columns,
        maximize_outcome=True,
        critical_difference="nemeyi",
    )
    diagram.to_file("plots/ExemploF1.pdf",
                    reverse_x=False,
                    )
