#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* FILE_NAME = "input.txt";
// each board has 5 columns
int COLS = 5;
// each board has 5 rows
int ROWS = 5;

void copy3d(size_t x, size_t y, size_t z, int d[x][y][z], int src[x][y][z]) {
  // copy a 3d array from src to dst
  memcpy(d, src, sizeof d[0] * x);
}

FILE* get_file() {
  // Open the input file and return file pointer
  FILE *fp;

  fp = fopen(FILE_NAME, "r"); // read only

  if (fp == NULL) {
    perror("Error while opening file.\n");
    exit(EXIT_FAILURE);
  }

  return fp;
}

char* get_input() {
  // Get input numbers from input file
  FILE *fp = get_file();

  // Get bingo numbers
  char *input;
  size_t len = 0;
  getline(&input, &len, fp);
  fclose(fp);
  return input;
}

void print_board(int (*boards)[COLS][ROWS], int board_num) {
  // print board <board_num> in boards <boards>
  for (int row=0; row<ROWS; row++) {
    for (int col=0; col<COLS; col++) {
      int val = boards[board_num][col][row];
      printf("%d ", val);
    }
    printf("\n");
  }
  printf("---\n");
}

int get_num_boards(int rows_per_board) {
  // figure out how many boards there are
  // each board is separated by a blank line (\n)
  // boards start on line 3 of input file and go on to line n
  FILE *fp = get_file();

  char *line;
  size_t len = 0;
  ssize_t read;
  getline(&line, &len, fp); // skip the first line which is input

  int num_lines = 0;
  while ((read = getline(&line, &len, fp)) != -1) {
    if (strcmp(line, "\n") == 0) {
      continue;
    } else {
      num_lines++;
    }
  }

  fclose(fp);
  return num_lines / rows_per_board;
}

void read_boards(int (*boards)[COLS][ROWS]) {
  // Read boards from input file into <boards>
  FILE *fp = get_file();

  char *line;
  size_t len = 0;
  ssize_t read;
  getline(&line, &len, fp); // skip the first line which is input
  getline(&line, &len, fp); // second line is a new line

  int board = 0; 
  int col = 0;
  int row = 0;
  while ((read = getline(&line, &len, fp)) != -1) {
    // read a row
    if (strcmp(line, "\n") == 0) {
      // row is empty, reset for next new board
      board++;
      row = 0;
      col = 0;
    } else {
      // process row
      char *tok;
      tok = strtok(line, " ");
      do {
        int num = atoi(tok);
        boards[board][col][row] = num;
        col++;
        tok = strtok(NULL, " ");
      } while (tok != NULL);
      // next row
      row++;
      col=0;
    }
  }
  fclose(fp);
}

void step(int (*boards)[COLS][ROWS], int num_boards, int num) {
  // take a step in the game
  // search for num in each board
  // if it's in the board, set that position to -1
  for (int board=0; board<num_boards; board++) {
    for (int col=0; col<COLS; col++) {
      for (int row=0; row<ROWS; row++) {
        if (boards[board][col][row] == num) {
          // boards can contain 0's but not negatives
          // we can use this as the marker
          boards[board][col][row] = -1;
        }
      }
    }
  }
}

int hasWon(int (*boards)[COLS][ROWS], int board_num) {
  // Check win conditions for a board

  // check columns
  for (int col=0; col<COLS; col++) {
    int col_sum = 0;
    for (int row=0; row<ROWS; row++) {
      col_sum += boards[board_num][col][row];
    }
    if (col_sum == (-1 * COLS)) {
      return 1;
    }
  }

  // check rows
  for (int row=0; row<ROWS; row++) {
    int row_sum = 0;
    for (int col=0; col<COLS; col++) {
      row_sum += boards[board_num][col][row];
    }
    if (row_sum == (-1 * ROWS)) {
      return 1;
    }
  }

  // check diags
  // int left_diag[5] = {
  //   {0, 0}, // col, row
  //   {1, 1},
  //   {2, 2},
  //   {3, 3},
  //   {4, 4}
  // };
  int left_diag_sum = 0;
  for (int i=0; i<ROWS; i++){
    left_diag_sum += boards[board_num][i][i];
  }
  if (left_diag_sum == (-1 * ROWS)) {
    return 1;
  }

  // int right_diag[5] = {
  //   {4, 0}, // col, row
  //   {3, 1},
  //   {2, 2},
  //   {1, 3},
  //   {0, 4},
  // }
  int right_diag_sum = 0;
  for (int i=0; i<ROWS; i++){
    right_diag_sum += boards[board_num][ROWS-i][i];
  }
  if (right_diag_sum == (-1 * ROWS)) {
    return 1;
  }

  return 0;
}

int get_board_sum(int board[COLS][ROWS]) {
  // Sum a marked board's values
  // does not include -1 (markers)
  int sum = 0;
  for (int row=0; row<ROWS; row++) {
    for (int col=0; col<COLS; col++) {
      if (board[col][row] == -1) {
        continue;
      }
      sum += board[col][row];
    }
  }
  return sum;
}

int play_games(char *input, int (*boards)[COLS][ROWS], int num_boards){
  // Play bingo for each board in <boards> using intputs <input>

  // make a copy to mutate
  int boards_copy[num_boards][COLS][ROWS];
  copy3d(num_boards, COLS, ROWS, boards_copy, boards);
  char *tok;
  tok = strtok(input, ",");

  do {
    int num = atoi(tok);
    // Run a step for each board
    step(boards_copy, num_boards, num);

    // check if any board has won
    for (int board=0; board<num_boards; board++) {
      if (hasWon(boards_copy, board)) {
        printf("board %d has won on num %d\n", board, num);
        printf("\nUnmarked board:\n---\n");
        print_board(boards, board);
        printf("\nMarked board:\n---\n");
        print_board(boards_copy, board);
        int sum = get_board_sum(boards_copy[board]);
        return sum * num;
      }
    }

    // get next input number
    tok = strtok(NULL, ",");
  } while (tok != NULL);
}

int main() {
  // Get bingo number
  char *input;
  input = get_input();

  // Get bingo boards
  int num_boards = get_num_boards(ROWS);
  int boards[num_boards][COLS][ROWS];
  read_boards(boards);

  // play games
  int board_score = play_games(input, boards, num_boards);
  printf("board score: %d\n", board_score);

  return 0;
}