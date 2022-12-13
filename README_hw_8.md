# HW 8

*_Modules `sys`, `os` task_*

This task is made by contributors: Elizaveta Gafarova, Dasha Golofeeva, Anastasia Lianguzova.

## There are following utilities in the repository:

- `wc` - prints newline, word and byte counts for the files;

- `ls` - lists computer files and directories;

- `sort`- prints the lines of its input in sorted order;

- `rm` - removes the input file;

- `grep` - searching text data sets for lines matching an input regular expression;

- `cat` - reads files sequentially, printing them in output;

- `tail` - prints the last few number of lines of a given file (10 lines by default);

- `mkdir` - creates a new directory;

- `cp` - copies files and directories;

- `mv` - moves existing file/directory to a new location;

- `uniq` - filters an input file removing duplicated lines from it.

The individual scripts could be downloaded from the repo, after that`chmod +x {file}` should be runned in terminal to make files executable. The repo also contains `install.py` script. Running it enables to run the scripts without providing their paths. 

Thus, to use above-mentioned utilities one should enter `{path_to}/utility_name.py` in a command line or, after using `install.py` script just `utility_name.py`. 

### UNIX utilities usage

1. `./install.py` - will not give any output in terminal but all files in a working directory will be copied to a PATH environment.  

2. `wc` can be used without options or with following options: *-w*, *-l*, *-c*.

`wc.py -w` counts words in a given file.

> `$ printf 'Hi\nthis is a test file' >> test.txt`
> 
> `$ wc.py -w test.txt`
> 
> *6*

`wc.py -l` counts lines in a file.

> `$ wc.py -l test.txt`
> 
> *1*

`wc.py -c` counts the number of bytes of a file.

> `$ wc.py -c test.txt`
> 
> *22*

`wc.py` without options counts everything and prints result in the following order: lines count, words count, bytes count!

> `$ wc.py test.txt`
> 
> *1 6 22*

2. `ls` can be used just as ls.py or with -a option. 

`ls.py` shows files located in a given directory (a working directory by default; in case of examples it is `python/hw_sys/scripts/`). 

>  `$ ls.py`
>
> *cat.py cp.py grep.py install.py ls.py mkdir.py mv.py rm.py sort.py tail.py uniq.py wc.py*
>
>  `$ ls.py ../../`
>
> *Untitled.ipynb data hw_fun hw_sys re_hw* </pre>

-a option enables to find hidden files (their name starts with a dot)

>  `$ ls.py ../../ -a`
>
> *.idea .ipynb_checkpoints Untitled.ipynb data hw_fun hw_sys re_hw*


3. `sort` used without options.

> `$ printf 'hyabc\ndef\nskkg' >> sort_test.txt`
> 
> `$ sort.py sort_test.txt`
> 
> *def*
> 
> *hyabc*
> 
> *skkg*


4. `rm` has one option: -r. 

Using `rm.py` without options remove a particular file. 

> `$ rm.py sort_test.txt`
> 
> `$ find . -name sort_test.txt` - will give an empty result.

`rm.py -r` removes entire directory with all files inside.

> `$ mkdir test`
> 
>  `$printf 'aaaaaaaaaaaa' >> ./test/aaaa.txt`
>  
>  `$ rm.py -r test`
>  
>  `$ find . -name sort_test.txt` - will give an empty result.

5. `grep` has no options. 

> `$ ls | grep.py '\w+\.py'` - will gives all python scripts in a directory.
> 
> *cat.py*
> 
> *cp.py*
> 
> *grep.py*
> 
> *install.py*
> 
> *ls.py*
> 
> *mkdir.py*
> 
> *mv.py*
> 
> *rm.py*
> 
> *sort.py*
> 
> *tail.py*
> 
> *uniq.py*
> 
> *wc.py*

6. `cat` has no options. The utility can read files or standard input. 

> `$printf 'i need a vacation' >> vacation.txt`
> 
> `$printf 'or i will go to work in pyaterochka' >> pyaterochka.txt`
> 
> `$ cat.py vacation.txt`
> 
> *i need a vacation*

`cat.py <file1> <file2>` will contacenate the files into one output. 

> `$ cat.py vacation.txt pyaterochka.txt`
> 
>  *i need a vacation*
>  
>  *or i will go to work in pyaterochka*

7. `tail.py <file>` will print the last lines of a file. It has one option: -n for a nuber of lines needed. You can also use the utility without its option, the default number of lines is 10.

> `$ printf 'Hi\nthis\nis\nanother\ntest\nfile\nwith\nten\ndamn\nlines' >> test1.txt`
> 
> `$ tail.py test1.txt`
> 
>  *Hi*
>  
>  *this*
>  
>  *is*
>  
>  *another*
>  
>  *test*
>  
>  *file*
>  
>  *with*
>  
>  *ten*
>  
>  *damn*
>  
>  *lines*
>
>`$ tail.py -n 2 test1.txt`
>
>  *damn*
>  
>  *lines*

  

















