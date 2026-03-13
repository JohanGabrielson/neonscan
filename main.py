import time
from scanner import scan_host
from network import get_hosts
import concurrent.futures
from output import banner, show_results, shutdown_message

def port_selection():
    print("\nMake a selection:")
    print("1) Quick scan (22, 80, 443)")
    print("2) Standard scan (22, 80, 443, 445, 3389)")
    print("3) Full scan (1–1024)")
    print("4) Custom port selection")

    choice = input("\nSelect: ").strip()

    if choice == "1":
        return [22, 80, 443]

    elif choice == "2":
        return [22, 80, 443, 445, 3389]

    elif choice == "3":
        return list(range(1, 1025))

    elif choice == "4":
        ports = input("Ports (ex: 21,22,80,443): ")
        try:
            return [int(p.strip()) for p in ports.split(",") if p.strip().isdigit()]
        except ValueError:
            print("Invalid. Try again.")
            return port_selectiion()

    else:
        print("Invalid selection. Try again.")
        return port_selection()


def main():
    banner()
    target = input("Enter IP or subnet: ")
    ports = port_selection()

    hosts = get_hosts(target)
    results = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        future_map = {executor.submit(scan_host, ip, ports): ip for ip in hosts}
        for future in concurrent.futures.as_completed(future_map):
            ip = str(future_map[future])
            results[ip] = future.result()

    show_results(results)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        shutdown_message()
        exit(0)

