## Rock Paper Scissors Vyper Game

player0: public(address)
player1: public(address)

player0Choice: public(uint256)
player1Choice: public(uint256)



player0ChoiceMade: public(bool)
player1ChoiceMade: public(bool)

winner: public(address)


@external
def __init__(_player1: address):
    self.player0 = msg.sender
    self.player1 = _player1


@external
def makeChoice(_choice: uint256):
    if msg.sender == self.player0:
        self.player0Choice = _choice
        self.player0ChoiceMade = True
    elif msg.sender == self.player1:
        self.player1Choice = _choice
        self.player1ChoiceMade = True


# calculate store and winner address
@external
def reveal():
    if self.player0ChoiceMade and self.player1ChoiceMade:
        if self.player0Choice == self.player1Choice:
            self.winner = ZERO_ADDRESS
        elif self.player0Choice == 0 and self.player1Choice == 1:
            self.winner = self.player1
        elif self.player0Choice == 0 and self.player1Choice == 2:
            self.winner = self.player0
        elif self.player0Choice == 1 and self.player1Choice == 0:
            self.winner = self.player0
        elif self.player0Choice == 1 and self.player1Choice == 2:
            self.winner = self.player1
        elif self.player0Choice == 2 and self.player1Choice == 0:
            self.winner = self.player1
        elif self.player0Choice == 2 and self.player1Choice == 1:
            self.winner = self.player0
        else:
            self.winner = ZERO_ADDRESS
   




@internal
def _resetChoices():
    self.player0Choice = 0
    self.player1Choice = 0
    self.player0ChoiceMade = False
    self.player1ChoiceMade = False


@external
def kill():
    assert msg.sender == self.player0 or msg.sender == self.player1
    selfdestruct(msg.sender)
