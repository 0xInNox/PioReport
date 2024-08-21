# Sample input data
data = """
JsJhJd:0.96
QsQhQd:5.04
8s2h2d:10.7
9s2s2h:11.16
5s3s3h:14.76
Ts3h3d:7.79
4s4h2d:9.99
4s4h3d:4.9
Qs4h4d:4.53
5s5h4d:12.5
7s5s5h:9.32
7s6h6d:11.48
As6s6h:5.25
As6h6d:6.04
7s7h6s:9.88
Ts7h7d:9.34
Ks7s7h:3.53
8s8h7d:10.15
Js8s8h:14.12
9s9h2s:3.14
9s9h6d:8.69
As9s9h:13.29
TsTh5s:6.13
TsTh7s:11.58
KsThTd:5.73
JsJh3d:13.82
KsJsJh:5.4
KsQhQd:12.85
KsKh5s:10.2
KsKh9s:7.83
KsKhJd:11.17
AsAh3s:5.82
AsAh4d:10.49
AsAhTd:13.25
5s3h2d:4.39
8s3h2s:11.68
Ts3h2s:5.48
Js3h2h:6.74
Ks3h2d:8.79
Ks3h2s:7.44
As3s2h:9.19
6s4h2h:11.54
6s4h2s:6.23
9s4h2s:14.44
Ts4h2h:12.57
Qs4s2h:4.21
6s5s2h:10.16
Ts5h2h:12.72
Qs5h2d:12.02
Ks5h2s:10.69
As5h2d:4.33
8s6h2d:10.61
Js6h2d:18.88
Js6s2s:10.7
Qs6h2s:4.4
Qs7h2h:21.93
As7h2d:9.04
As7s2h:14.72
9s8h2d:8.14
Qs8s2h:12.69
Ks8h2d:8.77
As8s2s:9.56
Ts9h2d:22.13
Ks9h2d:6.51
QsTs2h:4.38
KsJh2d:10.94
AsQh2h:10.18
AsKh2d:10.51
6s4h3d:1.38
6s4h3s:9.51
7s4h3h:12.58
7s4h3s:4.37
9s4h3d:8.55
Js4h3h:8.6
Ks4h3s:12.57
7s5h3d:11.39
8s5h3d:5.55
8s5s3s:6.92
Js5h3d:10.22
As5h3d:11.99
7s6h3h:4.3
7s6s3h:6.53
8s6h3d:5.09
9s6h3d:9
Ts6h3d:7.56
Qs6h3s:15.04
As7h3d:3.7
As7h3h:13.87
Ts8h3d:11.31
Js8h3s:6.6
Qs8h3d:4.67
Ts9h3d:1.78
Ts9s3s:9.8
Js9h3s:21.48
QsTh3d:14.5
KsTh3h:15.96
QsJs3h:13.53
KsQh3s:4.08
AsQs3h:11.47
6s5h4s:7.75
7s5h4h:4.91
7s5s4s:5.94
8s5h4d:8.93
Ts5h4d:16.71
Ks5s4h:5.39
As5s4s:6.59
Js6h4h:1.59
Ks6h4d:14.75
8s7s4s:10.93
9s7h4d:14.95
Qs7h4s:16.27
9s8h4s:13.77
Qs8h4s:7.78
Ks8s4h:15.63
As8h4d:8.66
Js9h4s:0.36
As9s4h:9.34
JsTh4h:12.86
AsTs4h:11.63
QsJh4d:19.08
KsJh4s:11.52
AsJh4s:11.73
7s6h5d:2.84
8s6s5h:12.53
9s6s5h:13.5
Ts7h5s:8.97
Js7h5d:10.37
9s8h5s:12.66
Js8h5h:14.68
Qs8h5s:10.46
As8h5d:0.43
As8h5s:11.34
Qs9h5d:23
Ks9h5s:3.46
Ks9s5h:4.45
JsTs5h:8.11
QsTs5s:5.93
AsJh5h:16.22
KsQh5d:5.61
AsKh5d:12.29
Ks7h6d:18.91
9s8h6h:10.84
As8h6d:15.78
Js9h6h:7.25
Qs9h6d:0.11
Qs9h6h:5.41
As9h6d:15.89
JsTh6d:12.21
QsTh6d:14.37
QsTh6s:6.08
KsTh6d:0.91
KsTh6h:18.8
QsJh6d:8.84
AsQh6h:10.96
AsKs6s:9.96
9s8h7s:2.13
Ts8h7s:11.76
Js8h7s:15.77
Ks8h7s:17.89
Ts9h7d:11.37
Js9s7h:12.2
Qs9s7h:5.13
Qs9s7s:10.62
Ks9s7h:7.31
JsTh7d:12.77
KsJh7s:0.29
KsQh7d:7.87
AsQh7d:5.59
Ts9h8h:6.29
Js9s8s:6.97
AsTh8d:1.13
AsTh8h:16.53
KsQh8d:13.38
AsQs8h:6.79
KsJs9h:11.31
AsJs9h:9.09
KsQs9h:15.33
AsKh9d:11.47
KsJsTs:7.93
AsJsTh:11.03
AsQhTs:8.35
AsKhTh:7.89
KsQsJh:4.74
AsQhJd:7.13
"""

# Parse and sort the data
def parse_and_sort(data):
    # Split the data into lines
    lines = data.strip().split('\n')
    
    # Create a list of tuples (hand, weight)
    entries = []
    for line in lines:
        hand, weight = line.split(':')
        weight = float(weight)
        entries.append((hand, weight))
    
    # Sort the list by weight in descending order
    sorted_entries = sorted(entries, key=lambda x: x[1], reverse=True)
    
    return sorted_entries

# Print the sorted data
def print_sorted_data(sorted_entries):
    for hand, weight in sorted_entries:
        print(f"{hand}:{weight:.2f}")

# Main execution
sorted_entries = parse_and_sort(data)
print_sorted_data(sorted_entries)
