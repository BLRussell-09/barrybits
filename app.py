import bencode
import os
import datetime
import hashlib
from types import SimpleNamespace

class t_decode():
  announce = ''
  announce_list = []
  comment = ''
  created_by = ''
  creation_date = 0
  encoding = ''
  info = []

  def decode_torrent(self):
    path = os.getcwd()
    path = path + '/stone.torrent'
    dt = bencode.bread(path)
    dt['announce_list'] = dt['announce-list']
    dt['created_by'] = dt['created by']
    dt['creation_date'] = dt['creation date']
    dt = SimpleNamespace(**dt)
    return dt

  def hash_info(self, tor):
    info = tor.info.pieces
    hashedinfo = hashlib.sha1(info).hexdigest()
    return hashedinfo

  def t_useable(self):
    t = self.decode_torrent()
    tor = self
    tor.announce = t.announce
    tor.announce_list = t.announce_list
    tor.comment = t.comment
    tor.created_by = t.created_by
    tor.creation_date = t.creation_date
    tor.encoding = t.encoding
    tor.info = SimpleNamespace(**t.info)
    return tor


t = t_decode().t_useable()
print(t.hash_info(t))