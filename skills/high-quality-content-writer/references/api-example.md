# AI Vetter API Example

Observed public Next.js server action from `https://tropes.fyi/vetter`.

Action id:

```text
404078c1891780d50bb636ae78e61eacced061b793
```

Call shape:

```bash
curl -s -X POST 'https://tropes.fyi/vetter' \
  -H 'Next-Action: 404078c1891780d50bb636ae78e61eacced061b793' \
  -H 'Content-Type: text/plain;charset=UTF-8' \
  --data-binary '["https://ossama.is/writing/tropes"]'
```

Response shape:

```text
0:{"a":"$@1","f":"","b":"Fdqox3rtkX690ahfCbTN1","q":"","i":false}
1:{"success":true,"result":{"url":"https://ossama.is/writing/tropes","title":"tropes.fyi: Name and shame AI writing","score":100,"verdict":"Pure AI Slop","verdictColor":"text-red-700","tropeCount":4,"totalMatches":20,"wordCount":743,"detections":[{"tropeId":"delve","tropeName":"\"Delve\" and Friends","category":"word-choice","matchCount":6,"matches":[{"tropeId":"delve","excerpt":"...","position":2176}]}],"id":"31d70d92"}}
```

Normalize the response to JSON with:

- `success`
- `error` when present
- `result.url`
- `result.title`
- `result.score`
- `result.verdict`
- `result.tropeCount`
- `result.totalMatches`
- `result.wordCount`
- `result.detections[]`
- `result.detections[].tropeId`
- `result.detections[].tropeName`
- `result.detections[].category`
- `result.detections[].matchCount`
- `result.detections[].matches[].excerpt`
- `result.detections[].matches[].position`

