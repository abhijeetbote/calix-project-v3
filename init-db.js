db = db.getSiblingDB("developer_db");
db.developer_tb.drop();

db.developer_tb.insertMany([
    {
        "id": 1,
        "name": "python",
        "type": "lang"
    },
    {
        "id": 2,
        "name": "java",
        "type": "tester"
    },
    {
        "id": 3,
        "name": "jenkins",
        "type": "cicd"
    },
]);