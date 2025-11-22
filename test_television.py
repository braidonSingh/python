import pytest
from television import *

def test_constructor():
    tv = Television()
    assert str(tv) == f"Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"

def test_power():
    tv = Television()
    tv.power()
    assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"
    tv.power()
    assert str(tv) == f"Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"

def test_mute():
    tv = Television()
    tv.power()
    assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"
    tv.mute()
    assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = 0"
    tv.mute()
    assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"
    tv.power()
    tv.mute()
    assert str(tv) == f"Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"

def test_channel_up():
    tv = Television()
    tv.power()
    assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"
    for i in range(Television.MIN_CHANNEL, Television.MAX_CHANNEL):
        assert str(tv) == f"Power = True, Channel = {i}, Volume = {Television.MIN_VOLUME}"
        tv.channel_up()
    # Channel should wrap after one more channel up.
    tv.channel_up()
    assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"
    tv.power()
    tv.channel_up()
    assert str(tv) == f"Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"

def test_channel_down():
    tv = Television()
    tv.power()
    assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"
    tv.channel_down()
    # Channel should've wrapped
    assert str(tv) == f"Power = True, Channel = {Television.MAX_CHANNEL}, Volume = {Television.MIN_VOLUME}"
    for i in range(Television.MAX_CHANNEL, Television.MIN_CHANNEL, -1):
        assert str(tv) == f"Power = True, Channel = {i}, Volume = {Television.MIN_VOLUME}"
        tv.channel_down()
    tv.channel_down()
    assert str(tv) == f"Power = True, Channel = {Television.MAX_CHANNEL}, Volume = {Television.MIN_VOLUME}"
    tv.power()
    tv.channel_down()
    assert str(tv) == f"Power = False, Channel = {Television.MAX_CHANNEL}, Volume = {Television.MIN_VOLUME}"
    
def test_volume_up():
    tv = Television()
    tv.power()
    assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"
    for i in range(Television.MIN_VOLUME, Television.MAX_VOLUME):
        assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {i}"
        tv.volume_up()
    assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MAX_VOLUME}"
    tv.volume_up()
    assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MAX_VOLUME}"
    tv.power()
    tv.volume_up()
    assert str(tv) == f"Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MAX_VOLUME}"
    tv.power()
    tv.volume_down()
    tv.mute()
    assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {0}"
    tv.volume_up()
    assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MAX_VOLUME}"

def test_volume_down():
    tv = Television()
    tv.power()
    assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"
    for i in range(Television.MIN_VOLUME, Television.MAX_VOLUME):
        tv.volume_up()
    for i in range(Television.MAX_VOLUME, Television.MIN_VOLUME, -1):
        assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {i}"
        tv.volume_down()
    assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"
    tv.volume_down()
    assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"
    tv.power()
    tv.volume_down()
    assert str(tv) == f"Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {0}"
    tv.volume_down()
    assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"
