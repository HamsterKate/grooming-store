SEARCH_FIELDS = {
    "groomer-list": [
        ("first_name", "First name"),
        ("last_name", "Last name"),
        ("qualification", "Qualification"),
    ],
    "service-list": [
        ("name", "Name"),
        ("service_type", "Type"),
    ],
    "pet-list": [
        ("name", "Name"),
        ("breed", "Breed"),
    ],
}

FIELD_LOOKUP = {
    "first_name": "first_name__icontains",
    "last_name": "last_name__icontains",
    "qualification": "qualifications__name__icontains",

    "name": "name__icontains",
    "service_type": "service_type__icontains",
    "breed": "breed__icontains",
}
