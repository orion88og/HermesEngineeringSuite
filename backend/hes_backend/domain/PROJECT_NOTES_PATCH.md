Extend Project with an engineering notes collection.

Create a lightweight note record/value object with:
- author: str
- category: str
- body: str
- created_at: datetime (UTC)

Add methods:
- add_note(author, category, body)
- remove_note(index)

Rules:
- author/category/body must not be blank.
- add_note() appends a note and calls touch().
- remove_note() removes by index and calls touch().
- Raise ValueError for invalid input.
- Raise IndexError for an invalid index.

Do not introduce persistence in this package.
