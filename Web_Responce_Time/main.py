import asyncio
import aiohttp
import time
import os


def user_input():
    try:
        user_url = normalize_url(input("Paste URL :"))
        asyncio.run(web_load_time(user_url))
    except Exception as e:
        print(f"Failed to connect to {user_url}: {e}")

async def web_load_time(user_url,show_feedback=True):
    '''Take URL From User And Check For Load Time Of Website To Give Score'''

    try:
        async with aiohttp.ClientSession() as session:
            start_time = time.perf_counter()
            async with session.get(user_url) as response:
                await response.read()
                load_time = time.perf_counter() - start_time
                
                print(f"\n URL: {user_url}\n Response: {response.status}\n Totall Load Time: {load_time:.3f}")

                if load_time < 0.5:
                    feedback = "🚀 Excellent"
                    score = "Score: 10/10"

                elif load_time < 1.0:
                    feedback = "🟢 Very Good"
                    score = "Score: 9/10"

                elif load_time < 2.0:
                    feedback = "✅ Good"
                    score = "Score: 8/10"

                elif load_time < 3.0:
                    feedback = "🟡 Average"
                    score = "Score: 6/10"

                elif load_time < 5.0:
                    feedback = "🟠 Slow"
                    score = "Score: 4/10"

                else:
                    feedback = "🔴 Very Slow"
                    score = "Score: 2/10"
                
                if show_feedback:
                    print(feedback)
                    print(score)

                return load_time
        
    except Exception as e:
        print(f"Failed to connect to {user_url}: {e}")
        return None
    
def compare_input():
    '''take two url as input to compair their load time'''
    user_url_one = normalize_url(input("Paste First URL :"))
    user_url_sec = normalize_url(input("Paste Second URL :"))

    asyncio.run(compair_load_time(user_url_one,user_url_sec))

async def compair_load_time(user_url_one,user_url_sec):
    '''Compair Two Website And Give FeedBack Accordingly'''

    load_time_one, load_time_sec = await asyncio.gather(
        web_load_time(user_url_one,show_feedback=False),
        web_load_time(user_url_sec,show_feedback=False)
    )
    
    if load_time_one < load_time_sec:
        print(f"{user_url_one} is faster.")

    elif load_time_sec < load_time_one:
        print(f"{user_url_sec} is faster.")

    else:
        print("Both websites have the same load time.")



#Free Time :)

def normalize_url(url):
    '''check wheather user enter full http link or just refrence, add https to the given link'''
    url = url.strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    if not url.endswith("/"):
        url += "/"

    return url


MENU = [
    ("Check Website Response Time",   user_input),
    ("Compair Web Load Time", compare_input),
    ("Exit",    None)
]

def main():

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" + "=" * 55)
        print(" Check Website Response Time ")
        print("=" * 55)
        for i, (label, _) in enumerate(MENU, 1):
            print(f"   {i}.  {label}")
        print("=" * 55)

        try:
            choice = int(input("\n  Enter option: ").strip())
        except (ValueError, KeyboardInterrupt):
            print("\n  Invalid input. Try again.")
            input("\n  Press Enter to continue...")
            continue

        if choice < 1 or choice > len(MENU):
            print("  Out of range.")
            input("\n  Press Enter to continue...")
            continue

        label, action = MENU[choice - 1]
        if action is None:
            print("\n  Goodbye!\n")
            break

        action()

        input("\n  Press Enter to return to menu...")

if __name__ == "__main__":
    main()