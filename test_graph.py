import matplotlib
from dna_features_viewer import (
	GraphicFeature,
	GraphicRecord,
	CircularGraphicRecord,
)

features = [
	GraphicFeature(
		start = 139, end = 480, strand =+ 1, color = "#ffd700", label = "v2"
	),
	GraphicFeature(
		start = 20,
		end = 500,
		strand =+ 1,
		color = "#ffcccc",
		label = "Gene 1 with a very long name",
	),
	GraphicFeature(
        start=400, end=700, strand=-1, color="#cffccc", label="Gene 2"
    ),
    GraphicFeature(
        start=600, end=900, strand=+1, color="#ccccff", label="Gene 3"
    ),
]

# plot and export a linear view of the construct
record = GraphicRecord(sequence_length = 1000, features = features)
ax, _ = record.plot(figure_width = 5)
ax.figure.savefig("graphic_record_defined_by_hand.png")

# plot and export a circuluar view of the construct
circular_record = CircularGraphicRecord(sequence_length = 1000, features = features)
ax2, _ = circular_record.plot(figure_width = 4)
ax2.figure.tight_layout()
ax2.figure.savefig("graphic_record_defined_by_hand_circular.png", bbox_inches = "tight")