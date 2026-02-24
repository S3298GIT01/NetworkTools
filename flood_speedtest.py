import subprocess
from multiprocessing import Pool

# --- CONFIGURATION ---
# A mix of Ocala and regional servers to spread the load
SERVERS = ["48657", "10444", "16620", "1779", "1776"] 
SESSIONS = 20  # Total sessions to run in parallel
# ---------------------

def run_speedtest(index):
    # Rotate through the server list for each session
    server_id = SERVERS[index % len(SERVERS)]
    print(f"[Session {index}] Targeting Server {server_id}...")
    
    try:
        # Running the official speedtest CLI
        subprocess.run(
            ["speedtest", "-s", server_id, "--accept-license", "--accept-gdpr"],
            capture_output=True, 
            text=True
        )
        return f"[Session {index}] Done (Server {server_id})"
    except Exception as e:
        return f"[Session {index}] Failed: {e}"

if __name__ == "__main__":
    print(f"🚀 Launching {SESSIONS} parallel sessions across {len(SERVERS)} regions...")
    
    with Pool(SESSIONS) as pool:
        results = pool.map(run_speedtest, range(SESSIONS))
    
    print("\nTest Complete. All sessions finished.")

