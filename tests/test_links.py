def test_add_and_get_links(client):
    client.post("/api/categories", json={"name": "Dinner", "color": "#999", "icon": "plate"})
    client.post("/api/ideas", json={
        "title": "Fancy dinner",
        "content": "Try Italian food",
        "category_id": 1
    })
    client.post("/api/links", json={"url": "http://restaurant.com", "type": "booking", "idea_id": 1})

    res = client.get("/api/ideas/1/links")
    assert res.status_code == 200
    data = res.get_json()
    assert data[0]["type"] == "booking"
