"""
    Inverted Index

    https://en.wikipedia.org/wiki/Inverted_index
    
    Inverted Index is used to locate records by using words/terms. It is of two types
    1) Record level inverted index - identifies the record that contans the word
    2) Word level inverted index - identifies the position of the word in a record

"""


def set_and_operation(set1: set, set2: set) -> set:
    result = set()
    for element in set2:
        if element in set1:
            result.add(element)
    return result


class RecordLevelInvertedIndex:

    def __init__(self) -> None:
        self.index = {} # For the time being we're using dict. this won't scale

    def write(self, text: str, record_id: int) -> None:
        words = text.split()
        trimmed_words = [word.strip() for word in words] # During search, I won't be worried much about spaces and line breaks
        for trimmed_word in trimmed_words:
            self.__write_to_index(trimmed_word, record_id)

    def __write_to_index(self, word: str, record_id: int):
        if word not in self.index.keys():
            self.index[word] = set()
        self.index[word].add(record_id)

    def search(self, term: str) -> int:
        words = term.split()
        trimmed_words = [word.strip() for word in words] # During search, I won't be worried much about spaces and line breaks
        found_documents = None
        for trimmed_word in trimmed_words:
            if found_documents is None:
                # Add all the documents for the first word
                found_documents = set()
                documents_with_word = self.__get_documents(trimmed_word)
                for document in documents_with_word:
                    found_documents.add(document)
            else:
                # Do a AND operation between previously found records and new word's records
                documents_with_word = self.__get_documents(trimmed_word)
                found_documents = set_and_operation(found_documents, documents_with_word)
                if len(found_documents) == 0: # Once empty, it's always empty during AND operations
                    return found_documents
        return found_documents
    
    def __get_documents(self, word: str) -> set:
        if word in self.index.keys():
            return self.index[word]
        return set()


if __name__ == '__main__':
    index = RecordLevelInvertedIndex()
    index.write(
        "In computer science, an inverted index (also referred to as a postings list, postings file, or inverted file)",
        1
    )
    index.write(
        "is a database index storing a mapping from content, such as words or numbers, to its locations in a table,",
        2
    )
    index.write(
        "or in a document or a set of documents (named in contrast to a forward index, which maps from documents to content)",
        3
    )
    index.write(
        ".[1] The purpose of an inverted index is to allow fast full-text searches, at a cost of increased processing when",
        4
    )
    index.write(
        "a document is added to the database.[2] The inverted file may be the database file itself, rather than its index.",
        5
    )
    index.write(
        "It is the most popular data structure used in document retrieval systems,[3] used on a large scale for example", 
        6
    )
    index.write(
        """
        in search engines. Additionally, several significant general-purpose mainframe-based database management systems 
        have used inverted list architectures, including ADABAS, DATACOM/DB, and Model 204""",
        7
    )
    print(index.index)
    print(index.search("search engines."))
