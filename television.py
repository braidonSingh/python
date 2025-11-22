class Television():
    """
    Mimics a television.
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles the TV's power state.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mutes the TV, does not affect volume.
        If the TV is off, it can not be muted.
        """
        if not self.__status:
            return
        self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increments the current channel, upon reaching
        the maximum channel wraps around back to the minimum channel.
        If the TV is off, the channel can not be changed.
        """
        if not self.__status:
            return
        if self.__channel == Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL
            return
        self.__channel += 1
        
    def channel_down(self) -> None:
        """
        Decrements the current channel, upon reaching 
        the minimum channel wraps around back to the maximum channel.
        If the TV is off, the channel can not be changed.
        """
        if not self.__status:
            return
        if self.__channel == Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL
            return
        self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increments the current volume. Can not exceed the maximum volume.
        If the TV is off, the volume can not be changed.
        Unmutes the TV.
        """
        if not self.__status:
            return
        self.__muted = False
        self.__volume = min(self.__volume + 1, Television.MAX_VOLUME)

    def volume_down(self) -> None:
        """
        Decrements the current volume. Can not exceed the minimum volume.
        If the TV is off, the volume can not be changed.
        Unmutes the TV.
        """
        if not self.__status:
            return
        self.__muted = False
        self.__volume = max(self.__volume - 1, Television.MIN_VOLUME)

    def __str__(self) -> str:
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume if not self.__muted else 0}"
