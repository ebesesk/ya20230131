<script>
  import { link } from 'svelte-spa-router'
  import fastapi from '../../lib/api';

  let yms_dn = []
  let _year = 1
  let dongs = []
  // let apt_names = []
  let apts = [{
    // id: undefined, 
    // 도로명: undefined, 
    // 법정동: undefined, 
    // 지번: undefined, 
    // 아파트: undefined
  }]
  let viewDong = true
  let aptNames = []
  function update_realestate() {
    let url = "/api/realestate/dbupdate"
    fastapi('get', url, {}, (json) => {
      yms_dn = json.yms_dn
      // console.log(yms_dn)
    })
  }
  
  function getAptList(_year) {
    console.log(_year)
    let url = "/api/realestate/aptlist"
    let params = {
      year: _year
    }
    fastapi('get', url, params, (json) => {
      // console.log(json)
      // apt_names = json.apt_names
      dongs = json.dongs
      apts = json.apts
      console.log(json)
      // getDongApts(apts)
    })
  }
  function getDongAptsList(dong) {
    let aptNames = []
    for (var i=0; i < apts.length; i++) {
      // console.log(apts[i])
      if ((dong === apts[i].법정동) && (!aptNames.includes(apts[i].아파트))) {
        aptNames.push(apts[i].아파트)
      }
    }
    // console.log(aptNames)
    return aptNames
  }
  
  function getDongApts(dong) {
    viewDong = dong
    aptNames = getDongAptsList(dong)
  }


</script>

<div class="container">


<div class="row">
  <div class="col yms_dn text-sm-end">
    <span>{#each yms_dn as yms}{yms},&nbsp{/each}</span>
    <button class="badge text-bg-light" on:click={update_realestate}>update</button>
  </div>
   
  <div class="input-group input-group-sm mb-3 mt-1 year">
    <span class="input-group-text" id="inputGroup-sizing-sm">년</span>
    <input bind:value={_year} type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm">
    <button class="btn btn-outline-secondary btn-lite btn-sm" on:click={getAptList(_year)}>검색</button>
  </div>

  <div class="col donglist">
  </div>
</div>


<div class="col">
  <div class="col">
    {#each dongs as dong}
      <button class="badge text-bg-light" on:click={getDongApts(dong)}>{dong}</button>
    {/each}
  </div>
  <!-- {#each apt_names as apt_name}
  <div class="col">
    <button class="badge text-bg-light" on:click={() => {viewDong = dong}}>{apt_name}</button>
  </div>
  {/each} -->
  <div class="col apt-info">
    {#each apts as apt}
      {#if apt.년 && viewDong === true}
        {apt.년}년
        {apt.월}월
        {apt.일}일 &nbsp;
        {apt.도로명} &nbsp;
        {apt.법정동} &nbsp;
        {apt.지번}
        {apt.아파트} &nbsp;
        거래금액: {apt.거래금액.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')} &nbsp;
        건축년도: {apt.건축년도} &nbsp;
        층: {apt.층}층
        전용면적: {apt.전용면적}m<sup>2</sup><br>
      {:else if apt.년 && apt.법정동 === viewDong}
        {apt.년}년
        {apt.월}월
        {apt.일}일 &nbsp;
        {apt.도로명} &nbsp;
        {apt.법정동} &nbsp;
        {apt.지번}
        {apt.아파트} &nbsp;
        거래금액: {apt.거래금액.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')} &nbsp;
        건축년도: {apt.건축년도} &nbsp;
        층: {apt.층}층
        전용면적: {apt.전용면적}m<sup>2</sup><br>
      {/if}
    {/each}
  </div>
</div>


</div>

<style>
 .input-group.year {
  width: 20%;
 }
  .container {
    font-size: smaller;
  }
  .col.apt-info {
    font-size: smaller;
  }
</style>