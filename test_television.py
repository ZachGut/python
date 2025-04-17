import pytest
from television import Television

def test_values():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power_on():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_power_off():
    tv = Television()
    tv.power()
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_vol_mute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_unmute():
    tv = Television()
    tv.power()
    tv.mute()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_off_mute():
    tv = Television()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_off_unmute():
    tv = Television()
    tv.mute()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_off_channel_up():
    tv = Television()
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_on_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

def test_channel_past_max():
    tv = Television()
    tv.power()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_off_channel_down():
    tv = Television()
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_channel_past_min():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

def test_off_volume_up():
    tv = Television()
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_on_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

def test_on_mute_volume_up():
    tv = Television()
    tv.power()
    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

def test_on_volume_past_max():
    tv = Television()
    tv.power()
    for i in range(500):
        tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 100"

def test_off_volume_down():
    tv = Television()
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_on_volume_down():
    tv = Television()
    tv.power()
    for i in range(100):
        tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 99"

def test_on_mute_volume_down():
    tv = Television()
    tv.power()
    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_on_volume_past_min():
    tv = Television()
    tv.power()
    for i in range(500):
        tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
