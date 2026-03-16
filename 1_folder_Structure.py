from graphviz import Digraph

def generate_folder_structure():
    dot = Digraph(comment = "Folder Structure")

    # Root directory
    dot.node("Root", "Root")

    # Subdirectories
    dot.node("Folder1", "Folder1")
    dot.node("Folder2", "Folder2")
    dot.node("SubFolder1", "SubFolder1")
    dot.node("SubFolder2", "SubFolder2")

    # Files
    dot.node("File1", "File1.txt", shape = "rectangle")
    dot.node("File2", "File2.txt", shape = "rectangle")

    # Define hierarchy
    dot.edge("Root", "Folder1")
    dot.edge("Root", "Folder2")
    dot.edge("Folder1", "SubFolder1")
    dot.edge("Folder2", "SubFolder2")
    dot.edge("SubFolder1", "File1")
    dot.edge("SubFolder2", "File2")

    # Save as PNG
    dot.edge("1_folder_structure"< format = "png", cleanup = True)

generate_folder_strcture()
