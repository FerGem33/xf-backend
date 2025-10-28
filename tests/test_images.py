def test_add_and_get_images(client):
    client.post("/api/categories", json={"name": "Photos", "color": "#444", "icon": "image"})
    client.post("/api/entries", json={
        "title": "Trip",
        "content": "Beautiful place",
        "category_id": 1
    })

    # Add image
    res = client.post("/api/images", json={"url": "http://photo.png", "entry_id": 1})
    assert res.status_code == 201

    # Get images for entry
    res2 = client.get("/api/entries/1/images")
    data = res2.get_json()
    assert len(data) == 1
    assert data[0]["url"].startswith("http")
