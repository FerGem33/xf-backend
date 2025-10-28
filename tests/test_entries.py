def test_add_entry(client):
    # Create category first
    client.post("/api/categories", json={"name": "Journal", "color": "#222", "icon": "note"})

    res = client.post("/api/entries", json={
        "title": "First Date",
        "content": "We went to the park.",
        "category_id": 1,
        "images": ["http://image.com/pic1.jpg"]
    })
    assert res.status_code == 201
    data = res.get_json()
    assert "id" in data


def test_get_entries(client):
    client.post("/api/categories", json={"name": "Trips", "color": "#111", "icon": "plane"})
    client.post("/api/entries", json={
        "title": "Beach Trip",
        "content": "Sunny day",
        "category_id": 1
    })
    res = client.get("/api/entries")
    assert res.status_code == 200
    data = res.get_json()
    assert len(data) == 1
    assert data[0]["title"] == "Beach Trip"
