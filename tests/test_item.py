from src.channel import Channel


# def test_print_info():
#     list = []
#     channel_id = 'UCX44TgNXmA_XcBEaeft2elA'
#     channel = Channel(channel_id)
#     # Вызовите метод print_info()
#     channel.print_info()
#     list.append(channel)
#     assert len(list) == 1


def test_Channel():
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    assert moscowpython.title == 'MoscowPython'
    # assert moscowpython.video_count == 707
    assert moscowpython.url == 'https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A'

def test_str():
    channel = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    expected_str = "MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)"
    assert str(channel) == expected_str

def test_add():
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    highload = Channel('UCwHL6WHUarjGfUM_586me8w')
    combined_channel = moscowpython + highload
    expected_subscribers = 2841
    assert combined_channel == expected_subscribers


