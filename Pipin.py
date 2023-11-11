# Import the py-and-id package
from py_and_id import *

# Define the symbols and annotations
symbols = {
    "Methane": Symbol("Methane", "circle", "blue"),
    "Steam": Symbol("Steam", "circle", "green"),
    "Air": Symbol("Air", "circle", "red"),
    "Reactor": Symbol("Reactor", "rectangle", "yellow"),
    "Heat Exchange": Symbol("Heat Exchange", "triangle", "orange"),
    "Heat Recovery Boiler": Symbol("Heat Recovery Boiler", "triangle", "orange"),
    "CO Shift Converter": Symbol("CO Shift Converter", "rectangle", "yellow"),
    "CO2 Wash Tower": Symbol("CO2 Wash Tower", "cylinder", "purple"),
    "Cryogenic Separation Unit": Symbol("Cryogenic Separation Unit", "cylinder", "purple"),
    "Hydrogen": Symbol("Hydrogen", "circle", "blue"),
    "Nitrogen": Symbol("Nitrogen", "circle", "red"),
    "Argon": Symbol("Argon", "circle", "red"),
    "Methane (Residual)": Symbol("Methane (Residual)", "circle", "blue")
}

annotations = {
    "T1": Annotation("T1", "600-700oC"),
    "T2": Annotation("T2", "KXXTC"),
    "T3": Annotation("T3", "Variable"),
    "T4": Annotation("T4", "Variable"),
    "T5": Annotation("T5", "Variable"),
    "T6": Annotation("T6", "Variable"),
    "P1": Annotation("P1", "101.3 kPa"),
    "P2": Annotation("P2", "Variable"),
    "P3": Annotation("P3", "3000 kPa")
}

# Define the pipes and connections
pipes = {
    "Pipe1": Pipe(symbols["Methane"], symbols["Reactor"], "blue"),
    "Pipe2": Pipe(symbols["Steam"], symbols["Reactor"], "green"),
    "Pipe3": Pipe(symbols["Air"], symbols["Reactor"], "red"),
    "Pipe4": Pipe(symbols["Reactor"], symbols["Heat Exchange"], "black"),
    "Pipe5": Pipe(symbols["Heat Exchange"], symbols["Heat Recovery Boiler"], "black"),
    "Pipe6": Pipe(symbols["Heat Recovery Boiler"], symbols["CO Shift Converter"], "black"),
    "Pipe7": Pipe(symbols["CO Shift Converter"], symbols["CO2 Wash Tower"], "black"),
    "Pipe8": Pipe(symbols["CO2 Wash Tower"], symbols["Cryogenic Separation Unit"], "black"),
    "Pipe9": Pipe(symbols["Cryogenic Separation Unit"], symbols["Hydrogen"], "blue"),
    "Pipe10": Pipe(symbols["Cryogenic Separation Unit"], symbols["Nitrogen"], "red"),
    "Pipe11": Pipe(symbols["Cryogenic Separation Unit"], symbols["Argon"], "red"),
    "Pipe12": Pipe(symbols["Cryogenic Separation Unit"], symbols["Methane (Residual)"], "blue")
}

connections = {
    "Pipe1": [annotations["T1"], annotations["P1"]],
    "Pipe2": [annotations["T1"], annotations["P1"]],
    "Pipe3": [annotations["T1"], annotations["P1"]],
    "Pipe4": [annotations["T2"]],
    "Pipe5": [annotations["T3"]],
    "Pipe6": [annotations["T4"]],
    "Pipe7": [annotations["T5"]],
    "Pipe8": [annotations["T6"]],
    "Pipe9": [annotations["P3"]],
    "Pipe10": [annotations["P2"]],
    "Pipe11": [annotations["P2"]],
    "Pipe12": [annotations["P2"]]
}

# Draw the diagram
diagram = Diagram(symbols, pipes, connections, annotations)
diagram.draw()
