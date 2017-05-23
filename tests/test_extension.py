
def test_hello():
    import emzed.ext
    reload(emzed.ext)
    assert emzed.ext.mass_plotter.hello().startswith("hello")
    