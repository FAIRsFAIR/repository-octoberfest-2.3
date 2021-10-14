## Usage 

Get token first using your login and password:
```
curl -X POST -H "Accept: application/json" \
	-H "Content-Type: application/json" \
	-d "{\"email\":\"your-email-here\",\"password\":\"your-password-here\"}" \
	https://fairsfair.fair-dtls.surf-hosted.nl/tokens
```

Use your token in this request to deposit metadata exposed as json-ld in the FAIR Data Point:
```
curl -H "Authorization: Bearer your-token-here" \
	-H "Content-Type: application/ld+json" \
	-d @export.json https://fairsfair.fair-dtls.surf-hosted.nl/dv-citation
```

Note: export files like export.json needs to be enriched with a dcterms:isPartOf statement, linking to the parent repository:
"dcterms:isPartOf": "https://fairsfair.fair-dtls.surf-hosted.nl",

