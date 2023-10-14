function makeTable(num_rows, num_cols) {
  return function() {
    var num_rows = document.tablegen.rows.value;
    var num_cols = document.tablegen.cols.value;
    var theader = '<table>\\n';
    var tbody = '';
    for (var i=0; i<num_rows;i++) {
      // create each row
      tbody += '<tr>';
      for (var j=0; j<num_cols;j++) {
        // create cell
        tbody += '<td>';
        tbody += 'Cell ' + i + ',' + j;
        tbody += '</td>'
      }
      // closing row table
      tbody += '</tr>\\n';
    }
    var tfooter = '</table>';
    // TO DO
    return theader + tbody + tfooter;
  }
}
