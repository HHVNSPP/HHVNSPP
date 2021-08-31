class Synergy():
    def __init__(self, nombre, technical, value, kind, lowerThreshold, upperThreshold, elementCount, active = False):
        self.nombre = nombre
        self.technical = technical
        self.value = value
        self.kind = kind
        self.lowerThreshold = lowerThreshold
        self.upperThreshold = upperThreshold
        self.elementCount = elementCount
        self.elements = []
        self.active = active

    def include(self, elem):
        self.elements.append(elem)
