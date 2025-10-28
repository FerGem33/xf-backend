def test_add_idea(client):
    client.post("/api/categories", json={"name": "Romantic", "color": "#f77", "icon": "heart"})

    res = client.post("/api/ideas", json={
        "title": "Picnic",
        "content": "In the garden with sandwiches",
        "category_id": 1,
        "links": [{"url": "http://maps.com/park", "type": "map"}]
    })
    assert res.status_code == 201
    data = res.get_json()
    assert "id" in data


def test_get_ideas(client):
    client.post("/api/categories", json={"name": "Adventures", "color": "#0088cc", "icon": "mountain"})
    client.post("/api/ideas", json={
        "title": "Skydiving",
        "content": "Crazy experience",
        "category_id": 1
    })
    res = client.get("/api/ideas")
    assert res.status_code == 200
    data = res.get_json()
    assert data[0]["title"] == "Skydiving"
