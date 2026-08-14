import pathlib


def test_signup_triggers_activity_refresh():
    app_js = pathlib.Path(__file__).resolve().parents[1] / "src" / "static" / "app.js"
    js_code = app_js.read_text()

    assert 'activitySelect.innerHTML = \'<option value="">-- Select an activity --</option>\';' in js_code
    assert 'await fetchActivities();' in js_code
    assert 'signupForm.reset();' in js_code
