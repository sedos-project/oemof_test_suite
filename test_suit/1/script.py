# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from oemof import solph
from datetime import datetime


class TestSuite:
    def __init__(self, periods):
        self.periods = periods

        self.setup_energysystem()
        self.add_components()

    def setup_energysystem(self):
        # create an energy system
        self.date_time_index = pd.date_range("1/1/2023", periods=self.periods,
                                             freq="H")
        self.energysystem = solph.EnergySystem(
            groupings=solph.GROUPINGS,
            timeindex=self.date_time_index,
            infer_last_interval=False)

    def add_components(self):
        es = self.energysystem

        # power bus
        bel = solph.Bus(label="bel")
        es.add(bel)

        # commodity 1
        com_1 = solph.Bus(label="com_1")
        es.add(com_1)

        # commodity 2
        com_2 = solph.Bus(label="com_2")
        es.add(com_2)

        # commodity 3
        com_3 = solph.Bus(label="com_3")
        es.add(com_3)

        # import source ts
        df = pd.read_csv("./input/commodities.csv", index_col=0)

        source_1 = solph.components.Source(
            label="source_1",
            outputs={com_1: solph.Flow(
                nominal_value=1,
                fix=df["com_1"]
            )},
        )
        es.add(source_1)

        source_2 = solph.components.Source(
            label="source_2",
            outputs={com_2: solph.Flow(
                nominal_value=1,
                fix=df["com_2"]
            )},
        )
        es.add(source_2)

        source_3 = solph.components.Source(
            label="source_3",
            outputs={com_3: solph.Flow(
                nominal_value=1,
                fix=df["com_3"]
            )},
        )
        es.add(source_3)

        sink = solph.components.Sink(
            label="sink_el",
            inputs={bel: solph.Flow()},
        )
        es.add(sink)

        conversion = solph.components.Transformer(
            label="conversion",
            inputs={com_1: solph.Flow(),
                    com_2: solph.Flow(),
                    com_3: solph.Flow(),
                    },
            outputs={bel: solph.Flow()},
            conversion_factors={
                com_1: 0.1,
                com_2: 0.2,
                com_3: 0.3,
                # bel: 0.1
            },
        )
        es.add(conversion)

        # create an optimization problem and solve it
        model = solph.Model(es)

        # solve model
        model.solve(solver="cbc")

        filename = f"./lp_files/{datetime.now().date()}.lp"
        model.write(filename, io_options={"symbolic_solver_labels": True})

        # create result object
        results = solph.processing.results(model)

        # plot the results
        plt.plot(results[(source_3, com_3)]["sequences"], label="commodity_3",
                 drawstyle="steps-post")
        plt.plot(results[(source_2, com_2)]["sequences"], label="commodity_2",
                 drawstyle="steps-post")
        plt.plot(results[(source_1, com_1)]["sequences"], label="commodity_1",
                 drawstyle="steps-post")

        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()
        plt.tight_layout()

        plt.show()


if __name__ == "__main__":
    a = TestSuite(periods=21)
