```console
python main.py -h
usage: logTime [-h] [--list] [--steps {STEPS_GLOBAL,STEPS_V1,STEPS_V2,STEPS_V3}] [--export] [--occurrences NUMBER_OF_OCCURRENCES] filepath

Parse logs and print out operation measures.

positional arguments:
  filepath

options:
  -h, --help            show this help message and exit
  --list                List available step lists
  --steps {STEPS_GLOBAL,STEPS_V1,STEPS_V2,STEPS_V3}
  --export              Export to CSV file
  --occurrences NUMBER_OF_OCCURRENCES
                        Number of occurrences to take into account
```

## examples:
To print out mesures with latest steps definition

```console
python main.py ../log_perfs/log_telpo_emv_2.txt --steps STEPS_V3
```

To export result to a CSV file to be used in a Google sheets/excel

```console
python main.py ../log_perfs/log_telpo_emv_2.txt --steps STEPS_V3 --export
```

To avoid the first slow cases to affect the result you can limit the number of (latest) occurrences taken into account

```console
python main.py ../log_perfs/log_telpo_emv_2.txt --steps STEPS_V3 --export --occurrences 20
```