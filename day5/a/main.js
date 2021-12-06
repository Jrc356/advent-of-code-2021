const { exit } = require('process')

fs = require('fs')

function get_segments(){
  const input = fs.readFileSync('input.txt', 'utf-8')
  const lines = input.split('\n')
  const segments = []

  for (let line of lines) {
    const split = line.split(' -> ')
    const x1y1 = split[0]
    const x2y2 = split[1]
    x1 = parseInt(x1y1.split(',')[0])
    y1 = parseInt(x1y1.split(',')[1])
    x2 = parseInt(x2y2.split(',')[0])
    y2 = parseInt(x2y2.split(',')[1])
    segments.push({
      x1,
      y1,
      x2,
      y2,
    })
  }
  return segments
}

function build_board(max_x, max_y) {
  const board = []
  for (let x=0; x<=max_x; x++) {
    board[x] = []
    for (let y=0; y<=max_y; y++) {
      board[x][y] = 0
    }
  }
  return board
}

function draw_segment(segment, board) {
  let dx = segment.x2 - segment.x1
  let dy = segment.y2 - segment.y1

  if (dx == 1 || dy == 1) {
    console.log('Segment delta = 1')
    console.log(segment)
  }

  let x = segment.x1
  let y = segment.y1

  while (dx != 0 || dy != 0) {
    board[x][y]++
    dx = segment.x2 - x
    dy = segment.y2 - y
    if (dx > 0) {
      x++
    } else if (dx < 0) {
      x--
    }
    if (dy > 0) {
      y++
    } else if (dy < 0) {
      y--
    }
  }
}

function main(){
  const segments = get_segments()
  
  // only care about horizontal or vertical lines
  const vh_segments = segments.filter((segment) => segment.x1 == segment.x2 || segment.y1 == segment.y2)
  console.log('Only vetical & horizontal segments: ', vh_segments.length)

  
  // draw each segment on a board
  console.log('Drawing segments')
  const max_x = 1000
  const max_y = 1000
  const board = build_board(max_x, max_y)
  for (let segment of vh_segments) {
    draw_segment(segment, board)
  }

  // find points with more than 1 line going through it
  console.log('Finding overlapping points')
  let overlapping_points = 0
  for (let x=0; x<max_x; x++) {
    for (let y=0; y<=max_y; y++) {
      if (board[x][y] >= 2) {
        overlapping_points++
      }
    }
  }

  console.log(overlapping_points)
}

main()