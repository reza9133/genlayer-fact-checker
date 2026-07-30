# v0.2.17
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

import urllib.request
from genlayer import *

class FactChecker(gl.Contract):
    last_claim: str
    last_verdict: str
    total_verifications: u256

    def __init__(self):
        self.last_claim = ""
        self.last_verdict = "NONE"
        self.total_verifications = u256(0)

    @gl.public.write
    def verify_claim(self, claim_text: str, source_url: str) -> str:
        # 1. Fetching the attributable source nondeterministically from the live web
        req = urllib.request.Request(source_url, headers={'User-Agent': 'GenLayer-Validator/1.0'})
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                # Reading the first 3000 characters of the webpage to save context window
                web_content = response.read().decode('utf-8')[:3000]
        except Exception as e:
            web_content = f"Failed to fetch source: {str(e)}"

        # 2. Forcing the LLM to verify strictly based on the fetched source
        prompt = f"""
        Analyze the following claim for factual accuracy strictly based on the fetched web source context below.
        
        Claim: "{claim_text}"
        
        Fetched Source Context ({source_url}):
        {web_content}

        Respond strictly in JSON format with two keys:
        - "verdict": either "REAL", "FAKE", or "UNVERIFIED"
        - "reason": a brief 1-sentence explanation referencing the provided source text.
        """
        
        res = gl.eq_principle.prompt_non_comparative(
            lambda: prompt,
            task="Fact check the submitted claim against the fetched web source and return verdict in JSON",
            criteria="The output must be a valid JSON containing 'verdict' and 'reason'."
        )
        
        self.last_claim = claim_text
        self.last_verdict = str(res)
        self.total_verifications = self.total_verifications + u256(1)
        
        return str(res)

    @gl.public.view
    def get_last_result(self) -> str:
        return self.last_verdict

    @gl.public.view
    def get_stats(self) -> u256:
        return self.total_verifications
