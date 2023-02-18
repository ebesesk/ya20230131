<script>
import { push } from "svelte-spa-router"
import fastapi from "../../../lib/api";
import Error from "../../../components/Error.svelte"
import { page, keyword } from "../../../lib/store"
import moment from "moment/min/moment-with-locales"
moment.locale('ko')

export let onSearch
let subject
let content

function post_question(event) {
event.preventDefault()
let url = "/api/question/create"
let params = {
    subject: '#쿼리#' + subject,
    content: content
}
fastapi('post', url, params,
    (json) => {
        get_question_list()
    },
    (json_error) => {
    error = json_error
    }
  )
}

function get_question_list() {
  let url = "/api/question/list"  
  let params = {
    page: 0,
    size: 50,
    keyword: '#쿼리#'
  }
  fastapi('get', url, params, (json) => {
    question_list = json.question_list
    console.log(question_list)
    console.log(question_list[0])
    }
  )
} 

function update_question(event) {
  event.preventDefault()
  let url = "/api/question/update"
  let params = {
    question_id: question_id,
    subject: subject,
    content: content
  }
  fastapi('put', url, params, 
    (json) => {
      get_question_list()
    },
    (json_error) => {
      error = json_error
    }
  )
}

function delete_question(_question_id) {
  let url = "/api/question/delete"
  let params = {
    question_id: _question_id
  }
  fastapi('delete', url, params, 
    (json) => {
      get_question_list()    
    },
    (err_json) => {
        error = err_json
    }
  )
}

let question_list = []
get_question_list()
// console.log(question_list)


function etcToString(q) {
  if (Object.keys(q).includes('etc')) {
    q.etc = q.etc.join(',')
    return q
  } else {
    return q
  }
}

function runQuery(_query) {
  let q = _query.replace(/'/gi, '"').replace('True', 'true')
  q = etcToString(JSON.parse(q))
  console.log(q)
//   console.log(JSON.stringify(JSON.parse(q)))
  $page = 0
  $keyword = JSON.stringify(q)
  
}


</script>
<div class="mb-3 table">
  <table class="table table-hover">
    <!-- <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">제목</th>
        <th scope="col">쿼리</th>
        <th scope="col"></th>
      </tr>
    </thead> -->
    <tbody>
      {#each question_list as question, index}
      <tr>
        <th scope="col">{
          moment(question.create_date).format("YYMMDD")}</th>
        <td class="subject" on:click={runQuery(question.content)}>
          {question.subject.replace('#쿼리#', '')}
        </td>
        <td class="query" on:click={runQuery(question.content)}>
          {question.content}
        </td>
        <td>
          <button class="badge text-bg-danger" on:click={delete_question(question.id)}>
            Del</button>
        </td>
      </tr>
      {/each}
    </tbody>
  </table>
</div>

<div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">제목</label>
  <input type="txt" class="form-control-sm" size="37" bind:value={subject} id="exampleFormControlInput1" placeholder="">
</div>
<div class="mb-3">
  <label for="exampleFormControlTextarea1" class="form-label"></label>
  <textarea class="form-control-sm" bind:value={content} id="exampleFormControlTextarea1" rows="1" cols="43"></textarea>
  <button class="btn btn-sm text-bg-primary" on:click={post_question}>작성</button>
</div>

<style>
div.table {
  font-size: small;
  vertical-align: middle;
}
tbody > tr > th {
  font-size: xx-small;    
}
td.subject {
  font-size: medium; 
  font-weight: bolder;
}
td.subject > button {
 width: 70px;
 height: 20px;
 text-align: center;
}
td.query {
  font-size: xx-small;
}
tbody > tr {
  cursor: pointer;
}
</style>