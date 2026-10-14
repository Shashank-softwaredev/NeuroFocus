# NeuroFocus core workflow status

**Audit date:** 2026-10-14
**Project root:** `C:\Users\CSC\OneDrive\Desktop\NeuroFocus-demo\neurofocus`
**Scoring:** 10 equally weighted end-to-end workflows. A workflow counts as verified only when its complete listed behavior has an automated or manual test; partial signaling/API tests do not pass a browser-media workflow.

| # | Core workflow | Status | Evidence / gap |
|---|---|---|---|
| 1 | HR and Candidate registration, login, role checks, and invalid credentials | Passed — automatically tested | `backend/smoke_test.py`: registration/login/JWT test and production HR invite test. Does not exercise the browser forms. |
| 2 | HR creates a room; valid participants join; invalid rooms and excess seats are rejected | Passed — automatically tested | Smoke tests cover HR-only room creation, invalid room, delayed/reverse WebSocket joins, and role/seat limits. The browser dashboard-to-room flow is not tested. |
| 3 | Pre-join camera/microphone permission, device selection, visible camera preview | Implemented — not yet verified | Lobby, device selectors, permission handling, and fresh-frame readiness exist in `frontend/static/room.js`. No successful real camera/browser run is available; screenshot showed a blank camera tile. |
| 4 | HR and Candidate see and hear each other over WebRTC | Implemented — not yet verified | SDP, ICE exchange, remote track playback, and audio unlock are implemented. No two-browser/device media test has been completed. |
| 5 | Camera/microphone controls and device reconnection work independently | Implemented — not yet verified | Track controls, device fallback, and camera reconnect are present. No physical-device control/reconnect test is recorded. |
| 6 | HR questions, Candidate answers, and room chat relay to the correct participant | Passed — automatically tested | Smoke tests exercise question/answer and chat relay, including invalid and duplicate answer handling. No browser UI test is recorded. |
| 7 | Either participant shares and stops screen sharing | Implemented — not yet verified | `getDisplayMedia`, track replacement, and share-state signaling exist. No browser permission or remote-render test is recorded. |
| 8 | Leave, peer departure, rejoin, and media recovery after interruption | Partially implemented | WebSocket departure and ICE-restart request signaling are smoke-tested. Actual media recovery/rejoin and HR end-for-everyone behavior are not verified. |
| 9 | HR receives explainable technical/session events with provenance | Partially implemented | Tab/media event relay is tested. The event log is browser-side and transient; this is not a durable audit history or a trust-score workflow. |
| 10 | Validated AI integrity detection and explainable trust-score history | Not implemented | README and source confirm there is no CV/ML detection model or trust-score calculation. Do not present this as an implemented feature. |

## Current percentages

- **Implemented coverage:** 9/10 = **90%**. This counts workflows with a real implementation, including partial and unverified implementations; it is not a pass rate.
- **Verified working:** 3/10 = **30%**. Only workflows 1, 2, and 6 have complete automated evidence in the current test suite. No full browser workflow is counted as manually verified.
- **80% verification target:** **Not met.** A camera/browser run, two-participant WebRTC call, and screen-share test are still required; TURN configuration is also required for dependable restrictive cross-network paths.

## Checks run on 2026-10-14

- `backend/.venv/Scripts/python.exe -m compileall -q main.py smoke_test.py` — passed.
- `backend/.venv/Scripts/python.exe smoke_test.py` — 6 tests passed (25.625 seconds); includes invalid WebSocket JWT rejection and no JWT query string.
- `node --check frontend/static/room.js` — passed.
- `node --check frontend/static/app.js` — passed.
- No physical camera/microphone, two-device, screen-share, deployed-service, or cross-network test was run in this audit.

## Security finding fixed in this audit

The WebSocket previously accepted the bearer JWT in its URL query string, where reverse proxies or access logs could retain it. The browser now sends an `auth` message as the first WebSocket frame; the server validates it before room membership, with a 10-second handshake timeout. The smoke suite rejects an invalid JWT and checks the frontend no longer constructs a `?token=` URL. No production data or credentials were changed.

## Remaining requirements for an end-to-end release check

1. Complete the two-session flow in current Chrome/Edge with working cameras and microphones; verify both video directions, both audio directions, independent controls, and cleanup.
2. Test screen share and camera reconnect after device interruption.
3. Repeat on separate networks using HTTPS and a verified TURN service; inspect the selected ICE candidate pair before claiming relay success.
4. Do not report AI detection accuracy until a supported model and a representative labeled test set have been implemented and measured, including false positives and false negatives.
