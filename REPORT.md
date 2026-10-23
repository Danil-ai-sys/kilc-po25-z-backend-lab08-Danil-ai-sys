# Report, lab 08

**Name:** Danil Sobar 
**Group:** PO 25-Z 
**Date:** 23.10.2026

## What works

- [x] TODO 1, 2: rooms. `pytest tests/test_rooms.py`: 4 passed
- [x] TODO 3: the storage keeps messages per room, the four shell lines behave as shown
- [x] TODO 4: the messages router under `/rooms/{room_id}/messages`
- [x] TODO 5: `/stats` counts users, rooms, messages, pins
- [x] TODO 6: my own test
- `pytest`: 22 passed, 0 failed
- [x] Bruno on a freshly started server: 26 of 26

## Three questions

1. Message 3 exists, but it belongs to another room. The request asks for message 3 specifically inside room 1. The storage checks both the message ID and `room_id`, so message 3 is not found in room 1. Returning 404 prevents messages from one room from being accessed through another room.

2. The client checks the `code` field in the response body.

   `GET /rooms/99/messages`:

   ```json
   {"detail": "Room 99 not found", "code": "room_not_found"}
   ```

   `GET /rooms/1/messages/99`:

   ```json
   {"detail": "Message 99 not found", "code": "message_not_found"}
   ```

3. FastAPI gets `room_id` from the router prefix:

   ```python
   router = APIRouter(
       prefix="/rooms/{room_id}/messages",
       tags=["messages"],
   )
   ```

   The prefix applies to every route in this router. FastAPI reads `room_id` from the URL path and passes it to each route function.

4. My test, broken on purpose
Paste what pytest tests/test_mine.py printed when get checked only the id. The E lines are enough.
if message.id == message_id and message.room_id == room_id: