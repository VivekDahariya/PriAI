from app.compiler.compiler import KnowledgeCompiler

compiler = KnowledgeCompiler()

compiled = compiler.compile(

    document_name="Machine Learning",

   chunks = [

    "Neural Networks are trained using Gradient Descent",

    "Loss Function is optimized by Gradient Descent",

    "Gradient Descent requires learning rate"

]

)

print("\nDOCUMENT")

print(compiled.document)

print("\nUNITS")

for u in compiled.units:

    print(u)

print("\nDICTIONARY")

print(compiled.dictionary.word_to_id)

print("\nHKR NODES")

print(len(compiled.hierarchy))

print("\nRELATIONS")

for relation in compiled.relations:
    print(relation)

