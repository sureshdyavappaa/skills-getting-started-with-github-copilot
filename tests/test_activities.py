def test_get_activities_returns_activity_dictionary(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert payload


def test_get_activities_includes_expected_activity_fields(client):
    # Arrange
    endpoint = "/activities"
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get(endpoint)

    # Assert
    assert response.status_code == 200
    payload = response.json()
    first_activity = next(iter(payload.values()))

    assert required_fields.issubset(first_activity.keys())
    assert isinstance(first_activity["participants"], list)
