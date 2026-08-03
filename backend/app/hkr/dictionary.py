class KnowledgeDictionary:

    def __init__(self):

        self.word_to_id = {}
        self.id_to_word = {}

        self.counter = 1

    def get_id(self, value: str):

        if value not in self.word_to_id:

            key = f"D{self.counter}"

            self.counter += 1

            self.word_to_id[value] = key
            self.id_to_word[key] = value

        return self.word_to_id[value]

    def resolve(self, key: str):

        return self.id_to_word.get(key)

    def encode_metadata(self, metadata: dict):

        encoded = {}

        for k, v in metadata.items():

            if isinstance(v, str):

                encoded[k] = self.get_id(v)

            else:

                encoded[k] = v

        return encoded

    def decode_metadata(self, metadata: dict):

        decoded = {}

        for k, v in metadata.items():

            if isinstance(v, str) and v.startswith("D"):

                decoded[k] = self.resolve(v)

            else:

                decoded[k] = v

        return decoded