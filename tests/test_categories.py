def test_add_category(client):
    response = client.post("/api/categories", json={
        "name": "Romantic",
        "color": "#ff99cc",
        "icon": "heart"
    })
    assert response.status_code == 201
    assert b"created successfully" in response.data


def test_get_categories(client):
    client.post("/api/categories", json={"name": "Travel", "color": "#0099ff", "icon": "plane"})
    res = client.get("/api/categories")
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)
    assert data[0]["name"] == "Travel"


def test_update_category(client):
    client.post("/api/categories", json={"name": "Food", "color": "#00ff00", "icon": "apple"})
    res = client.put("/api/categories/1", json={"name": "Updated Food"})
    assert res.status_code == 200
    assert b"updated successfully" in res.data


def test_delete_category(client):
    client.post("/api/categories", json={"name": "Books", "color": "#aaaaaa", "icon": "book"})
    res = client.delete("/api/categories/1")
    assert res.status_code == 200
    assert b"deleted successfully" in res.data
