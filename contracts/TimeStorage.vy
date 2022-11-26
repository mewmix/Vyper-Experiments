event DataChange:
    setter: indexed(address)
    value: int128

storedData: public(int128)

startTime: public(uint256)
endTime: public(uint256)
startblock : public(uint256)



@external
def __init__(_x: int128, startTime: uint256):
  self.storedData = _x
  self.startTime = startTime
  self.endTime = block.timestamp + startTime
  self.startblock = block.timestamp 


@external
def set(_x: int128):
  assert _x >= 0, "No negative values"
  assert block.timestamp >= self.endTime, "Too Early"
  assert self.storedData < 100, "Storage is locked when 100 or more is stored"
  self.storedData = _x
  log DataChange(msg.sender, _x)

@external
def reset():
  assert block.timestamp >= self.endTime, "Too early"

  self.storedData = 0


