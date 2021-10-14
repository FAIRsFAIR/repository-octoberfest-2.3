# FAIRsFAIR Hackathon on FAIR enabling repositories

## Description of the workshop: 
Goal is to get the latest FAIR Data Point protocol supported by 1 or 2 of the working repositories selected by FAIRsFAIR in the beginning of the project, showing and proving interoperability between different implementations and automatic integration of catalogue information from different implementations. 
We would like to have technical people from the repositories on board, so that the implementation that will be worked on could be a branch of the official code, being close to an actual implementation by the running deployment of the repositories later.
Note that what we’re striving for is adding an FDP API, not replacing any existing repository functionality but adding an additional way that makes repositories more semantically interoperable and machine actionable.
If implemented in the repository software, a sandbox/dev environment of the repository software you are right now using.

 They need commit rights to your codebase or at the very least access to the source to be able to fork or branch. Experience with when extending your own repository with FDP functionality: 
- the repository software codebase, specifically adding new API endpoints RDF (if not with turtle/n3/RDF XML, then JSON-LD, or at the very least familiarity with JSON)
If looking at the reference implementation for inspiration, then java and spring-boot when deploying the reference implementation:
- basic sysadmin knowledge (example docs are based on Linux)
- docker / docker-compose 
