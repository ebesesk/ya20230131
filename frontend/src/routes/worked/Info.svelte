<script>
  import fastapi from "../../lib/api";
//   import { workedKeywords } from "../../lib/store";
  import { onMount } from "svelte";
  import Error from "../../components/Error.svelte"
  export let yearInfo
  export let monthInfo
  export let dayInfo
  export let noteInfo
  export let keywords = []
  let noteInfo2
//   get_note(yearInfo, monthInfo, dayInfo)
//   export search_worked
  let error = {detail:[]}
  let note = ''

//   console.log(yearInfo, monthInfo, dayInfo, noteInfo, '00000')
  
  function del_worked() {
    if(window.confirm('정말로 삭제하시겠습니까?')) {  
      let url = "/api/worked/delete_ymd"
      let params = {
        year: yearInfo,
        month: monthInfo,
        day: dayInfo
      }
      fastapi('delete', url, params, 
        (json) => {
          window.location.reload()
        //   dispatch('reload', {
        //     year: params.year,
        //     monthInfo: params.month - 1
        //   })
        //   console.log(params.year, params.month)
        },
        (json_error) => {
            error = json_error
        }
      )
    }
  }

  function create_worked() {
    let url = '/api/worked/create'
    let params = {
        year: yearInfo,
        month: monthInfo,
        day: dayInfo,
        note: note
    }
    fastapi('post', url, params, 
      (json) => {
        window.location.reload()
        // reload(params.year, params.month)
      },
      (json_error) => {
        error = json_error
      }
    )
  }

  function update_worked() {
    let url = '/api/worked/update'
    let params = {
        year: yearInfo,
        month: monthInfo,
        day: dayInfo,
        note: note,
    }
    fastapi('put', url, params, 
      (json) => {
        window.location.reload()
      },
      (json_error) => {
        error = json_error
      }
    )
  }
//   const noteInfo = () => {
//     let params = {
//       year: year,
//       month: month,
//       day: day
//     }
//     fastapi('get', '/api/worked/detail', params, (json) => {
//         return json.note
//       }
//     )
//   }
//   onMount(async() => {
//     let params = {
//       year: yearInfo,
//       month: monthInfo,
//       day: dayInfo
//     }
//     fastapi('get', '/api/worked/detail', params, (json) => {
//         noteInfo = json.note
//         // return json.note
//         console.log(note)
//       }
//     )
//   })
//   function get_note(year, month, day) {
//     console.log(year, month, day)
//     let params = {
//       year: year,
//       month: month,
//       day: day
//     }
//     fastapi('get', '/api/worked/detail', params, (json) => {
//         noteInfo = json.note
//         // return json.note
//         console.log(note)
//       }
//     )
//   }
//   get_note(yearInfo, monthInfo, dayInfo)
</script>
<Error error={error}/>
<!-- <input bind:value={yearInfo} class="form-control form-control-sm" type="number" placeholder="year" aria-label=".form-control-sm example">
<input bind:value={monthInfo} class="form-control form-control-sm" type="number" placeholder="month" aria-label=".form-control-sm example">
<input bind:value={dayInfo} class="form-control form-control-sm" type="number" placeholder="day" aria-label=".form-control-sm example"> -->
{yearInfo}년{monthInfo}월{dayInfo}일
{#each keywords as keyword}
  {keyword}
<!-- <label>
    <input type="radio", class="form-check-input" bind:group={note} value={keyword}>{keyword}
  </label> -->
{/each}
<div> 
  {#if noteInfo}
  <input class="form-control form-control-sm" bind:value={note} type="text" placeholder="{noteInfo}" aria-label=".form-control-sm example">
  <br>
  <button class="btn btn-sm  btn-primary" on:click={update_worked}>수정</button>
  <button class="btn btn-sm  btn-danger" on:click={del_worked}>삭제</button>
  {:else}
  <input class="form-control form-control-sm" bind:value={note} type="text" aria-label=".form-control-sm example">
  <br>
  <button class="btn btn-sm  btn-primary" on:click={create_worked}>추가</button>
  {/if}
</div>
