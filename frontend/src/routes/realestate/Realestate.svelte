<script>
  import { link } from 'svelte-spa-router'
  import fastapi from '../../lib/api';

  let yms_dn = []
  let _year = 1
  // let apt_names = []
  let apts = [{
    // id: undefined, 
    // 도로명: undefined, 
    // 법정동: undefined, 
    // 지번: undefined, 
    // 아파트: undefined
  }]
  function update_realestate() {
    let url = "/api/realestate/dbupdate"
    fastapi('get', url, {}, (json) => {
      yms_dn = json.yms_dn
      // console.log(yms_dn)
    })
  }
  
  function getAptsList(_year) {
    console.log(_year)
    let url = "/api/realestate/aptlist"
    let params = {
      year: _year,
      _sort: _sort
    }
    fastapi('get', url, params, (json) => {
      // console.log(json)
      // apt_names = json.apt_names
      dongs = json.dongs
      apts = json.apts
      dongs.sort()
      // console.log(json)
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
    console.log(aptNames)
    aptNames.sort()
    return aptNames
  }
  
  function viewDong(dong) {
    isDong = true
    isApt = false
    _viewDong = dong
    aptNames = getDongAptsList(dong)
  }
  function viewApt(aptName) {
    isDong = false
    isApt = true
    _viewApt = aptName
  }
  
  function viewAll() {
    isDong = false
    isApt = false
  }
  
  let isDong = false
  let isApt =false
  let dongs = []
  let aptNames = []
  let _viewDong 
  let _viewApt

  function sortPrice() {
    apts.sort((a,b) => {
      if(Number(a.가격) > Number(b.가격)) return 1
      if(Number(a.가격) < Number(b.가격)) return -1
      return 0
    })

    // apts.sort(function(a, b) {
    //   return a.가격 < b.가격 ? -1 : a.가격 > b.가격 ? 1 : 0
    // })
    // apts.sort(가격)

    // apts.sort(function (a, b) {
    //   if (a.가격 > b.가격) {
    //     return 1
    //   }
    //   if (a.가격 < b.가격) {
    //     return -1
    //   }
    //   return 0
    // })

    // apts = apts.sort((a, b) => a.가격 - b.가격)
    
    console.log(apts)
    return apts
  }

  let _sort
//  $:apts
</script>

<div class="container-fluid">
  
  
  <div class="row">
    <div class="col yms_dn text-sm-end">
      <span>{#each yms_dn as yms}{yms},&nbsp{/each}</span>
    <button class="badge text-bg-light" on:click={update_realestate}>update</button>
   </div>
   
    <div class="col input-group input-group-sm mb-3 mt-1 year">
      <span class="input-group-text" id="inputGroup-sizing-sm">정렬</span>
      <select class="form-select form-select-sm" bind:value={_sort} aria-label=".form-select-sm example" 
      on:change="{() => {console.log(_sort)}}">
        <!-- <option selected>거래일</option> -->
        <option value="{'date'}">거래일</option>
        <option value="{'price'}">가격</option>
        <option value="{'area'}">전용면적</option>
        <option value="{'construction'}">건축년도</option>
      </select>
      <span class="input-group-text" id="inputGroup-sizing-sm">년</span>
      <input bind:value={_year} type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm">
      <button class="btn btn-outline-secondary btn-lite btn-sm" on:click={getAptsList(_year)}>검색</button>
    </div>

  <!-- <div class="col donglist">
  </div> -->
  </div>


<div class="col">
  <div class="col">
    <!-- <button class="badge text-bg-success" on:click={sortPrice}>가격</button>
    <button class="badge text-bg-success" on:click={sortPrice}>건축년도</button>
    <button class="badge text-bg-success" on:click={sortPrice}>전용면적</button> -->
    {#if apts[0].년}
    <button class="badge text-bg-warning" on:click={viewAll}>all</button>
    {/if}
    {#each dongs as dong}
      <button class="badge text-bg-light" on:click={viewDong(dong)}>{dong}</button>
    {/each}
    {#each aptNames as aptName}
    <button class="badge text-bg-info" on:click={viewApt(aptName)}>{aptName}</button>
    {/each}
  </div>
  <!-- {#each apt_names as apt_name}
  <div class="col">
    <button class="badge text-bg-light" on:click={() => {viewDong = dong}}>{apt_name}</button>
  </div>
  {/each} -->
  <div class="col apt-info">
    {#each apts as apt}
      {#if apt.년 && isDong === false && isApt === false}
        {apt.년}{apt.월.toString().padStart(2,'0')}{apt.일.toString().padStart(2,'0')}
        {apt.도로명}
        {apt.법정동}
        <!-- {apt.지번} -->
        <span class="text-danger">{apt.아파트}</span>
        {apt.거래금액.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')}
        {apt.건축년도}
        {apt.층}층
        {Math.ceil(apt.전용면적)}m<sup>2</sup><br>
      {:else if apt.년 && isDong === true && apt.법정동 === _viewDong}
        {apt.년}{apt.월.toString().padStart(2,'0')}{apt.일.toString().padStart(2,'0')}
        <!-- {apt.년}년 -->
        <!-- {apt.월}월 -->
        <!-- {apt.일}일 -->
        {apt.도로명}
        {apt.법정동}
        <!-- {apt.지번} -->
        <span class="text-danger">{apt.아파트}</span>
        {apt.거래금액.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')}
        {apt.건축년도}
        {apt.층}층
        {Math.ceil(apt.전용면적)}m<sup>2</sup><br>
      {:else if apt.년 && isApt === true && apt.아파트 === _viewApt}
        {apt.년}{apt.월.toString().padStart(2,'0')}{apt.일.toString().padStart(2,'0')}
        <!-- {apt.년}년 -->
        <!-- {apt.월}월 -->
        <!-- {apt.일}일 -->
        {apt.도로명}
        {apt.법정동}
        <!-- {apt.지번} -->
        <span class="text-danger">{apt.아파트}</span>
        {apt.거래금액.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')}
        {apt.건축년도}
        {apt.층}층
        {Math.ceil(apt.전용면적)}m<sup>2</sup><br>
      {/if}
    {/each}
  </div>
</div>


</div>

<style>
 .input-group.year {
  height: 20px;
  width: 20%;

 }
 .form-select {
   height: 30px;
   font-size: xx-small;
 }
  .container-fluid {
    font-size: smaller;
  }
  .col.apt-info {
    font-size: smaller;
  }
</style>