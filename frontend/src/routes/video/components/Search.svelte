<script>
  import fastapi from "../../../lib/api";
  import { page, keyword } from "../../../lib/store"

  let kw = 'test2'
  let size = 20
  let none

  function get_videos_list() {
    let params = {
      page: $page,
      size: size,
      keyword: $keyword,
    }
    fastapi('get', '/api/video/list', params, (json) => {
      // console.log(json)
      video_list = json.video_list
      total = json.total
      kw = $keyword
    })
  }
  
  export let video = {
    resolution: [],
    display_quality: [],
    country: [],
    face: [],
    look: [],
    age: [],
    pussy: [],
    etc: "test2",
    
  }
  

  function onSearch() {
    let video_json = JSON.stringify(video)
    $keyword = video_json
    $page = 0
  }
  
  function allSelect() {
    video = {
      resolution: ["high","middle","low"],
      display_quality: ["아주좋음","좋음","보통","흐릿","폐기"],
      country: ["한국","일본","중국","서양","기타"],
      face: ["선명","흐릿"],
      look: ["마름","보통","뚱"],
      age: ["어림","학생","아가씨","아줌마","나이많음"],
      pussy: ["선명","흐릿"],
      etc: ""
    }
  }
  function allUnselect() {
    video = {
      resolution: [],
      display_quality: [],
      country: [],
      face: [],
      look: [],
      age: [],
      pussy: [],
      etc: ""
    }
  }
  
</script>
<div> 
  <br>
  <div class="header-button">
    <button on:click={allSelect} style="font-size: smaller; text-align: right;">모두선택</button>
    <button on:click={allUnselect} style="font-size: smaller; text-align: right;">모두선택해제</button>
    <form on:submit|preventDefault={onSearch}>
      <label>
        ect: <input type="text" bind:value={video.etc}><br>
      </label>
    </form>
    <button on:click={onSearch} style="font-size: smaller; text-align: right;">검색</button>
  </div>
  <!-- <div style="font-size: smaller;">
    <input type="text" class="form-control-sm" style="font-size: smaller;" bind:value="{kw}">
    <button class="btn btn-primary" style="font-size: smaller;" on:click={() => {$keyword = kw, $page = 0}}>검색</button>
  </div> -->
  <div class="justify-content-end" style="font-size: smaller;">
      해상도:
      <label>
        <input type="checkbox" class="form-check-input text-danger" bind:group={video.resolution} value="high" >고
      </label>
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.resolution} value="middle">중
      </label>
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.resolution} value="low">저
      </label>
      <label class="text-danger font-weight-bold">
        <input type="checkbox" class="form-check-input" bind:group={video.resolution} value="not">not
      </label>
      <br>
      화&nbsp;&nbsp;질:
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.display_quality} value="아주좋음" >아주좋음
      </label>
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.display_quality} value="좋음">좋음
      </label>
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.display_quality} value="보통">보통
      </label>
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.display_quality} value="흐릿">흐릿
      </label>
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.display_quality} value="폐기">폐기
      </label>
      <label class="text-danger font-weight-bold">
        <input type="checkbox" class="form-check-input" bind:group={video.display_quality} value="not">not
      </label>
      <br>
      국&nbsp;&nbsp;가:
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.country} value="한국" >한국
      </label>
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.country} value="일본">일본
      </label>
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.country} value="중국">중국
      </label>
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.country} value="서양">서양
      </label>
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.country} value="기타">기타
      </label>
      <label class="text-danger font-weight-bold">
        <input type="checkbox" class="form-check-input" bind:group={video.country} value="not">not
      </label>
      <br>
      얼&nbsp;&nbsp;굴:
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.face} value="선명" >선명
      </label>
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.face} value="흐릿">흐릿
      </label>
      <label class="text-danger font-weight-bold">
        <input type="checkbox" class="form-check-input" bind:group={video.face} value="not">not
      </label>
      <br>
      외&nbsp;&nbsp;모:
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.look} value="마름">마름
      </label>
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.look} value="보통">보통
      </label>
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.look} value="뚱">뚱
      </label>
      <label class="text-danger font-weight-bold">
        <input type="checkbox" class="form-check-input" bind:group={video.look} value="not">not
      </label>
      <br>
      나&nbsp;&nbsp;이:
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.age} value="어림" >어림
      </label>
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.age} value="학생">학생
      </label>
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.age} value="아가씨">아가씨
      </label>
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.age} value="아줌마">아줌마
      </label>
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.age} value="나이많음">많음
      </label>
      <label class="text-danger font-weight-bold">
        <input type="checkbox" class="form-check-input" bind:group={video.age} value="not">not
      </label>
      <br>
      ㅂ&nbsp;&nbsp;ㅈ:
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.pussy} value="선명" >선명
      </label>
      <label>
        <input type="checkbox" class="form-check-input" bind:group={video.pussy} value="흐릿">흐릿
      </label>
      <label class="text-danger font-weight-bold">
        <input type="checkbox" class="form-check-input" bind:group={video.pussy} value="not">not
      </label>
    </div>
    <br>
    
    
    
    
    
    
    
    <div class="row" style="font-size: smaller;">
      <div class="col radio-c" >
        <label>
          <input type="radio" name="school_uniform" bind:group={video.school_uniform} value={true}>교복 
        </label><br>
        <label class="text-danger font-weight-bold">
          <input type="radio" name="school_uniform" bind:group={video.school_uniform} value = {false}>교복 
        </label>
      </div>
      <div class="col radio-c">
        <label>
          <input type="radio" name='hip' bind:group={video.hip} value={true}>hip 
        </label><br>
        <label class="text-danger font-weight-bold">
          <input type="radio" name='hip' bind:group={video.hip} value={false}>hip 
        </label>
      </div>
      <div class="col radio-c">
        <label>
          <input type="radio" name='group' bind:group={video.group} value={true}>그룹
        </label>
        <label class="text-danger font-weight-bold">
          <input type="radio" name='group' bind:group={video.group} value={false}>그룹 
        </label>
      </div>
      <div class="col radio-c">
        <label>
          <input type="radio" name='pregnant' bind:group={video.pregnant} value={true}>임신 
        </label>
        <label class="text-danger font-weight-bold">
          <input type="radio" name='pregnant' bind:group={video.pregnant} value={false}>임신 
        </label>
      </div>
      <div class="col radio-b">
        <button on:click={() => {video.school_uniform = none
                                  video.hip = none
                                  video.group = none
                                  video.pregnant = none
                                }}>
          clear</button><br><br><br>
        </div>
      </div>
      
      
      
      
      <div class="row" style="font-size: smaller;">
        <div class="col radio-c">
          <label>
            <input type="radio" name='conversation' bind:group={video.conversation} value={true}>대화 
          </label>
          <label class="text-danger font-weight-bold">
            <input type="radio" name='conversation' bind:group={video.conversation} value={false}>대화
          </label>
        </div>
        <div class="col radio-c">
          <label>
            <input type="radio" name='lesbian' bind:group={video.lesbian} value={true}>레즈
          </label>
          <label class="text-danger font-weight-bold">
            <input type="radio" name='lesbian' bind:group={video.lesbian} value={false}>레즈 
          </label>
          <!-- <label class="text-danger font-weight-bold">
            <input type="radio" name='lesbian' group={video.lesbian} value={none}>레&nbsp;&nbsp;즈 
          </label> -->
        </div>
        <div class="col radio-c">
          <label>
            <input type="radio" name='ani' bind:group={video.ani} value={true}>에니
          </label>
          <label class="text-danger font-weight-bold">
            <input type="radio" name='ani' bind:group={video.ani} value={false}>에니
          </label>
        </div>
        <div class="col radio-c">
          <label>
            <input type="radio" name='oral' bind:group={video.oral} value={true}>입&nbsp;&nbsp;&nbsp;&nbsp; 
          </label>
          <label class="text-danger font-weight-bold">
            <input type="radio" name='oral' bind:group={video.oral} value={false}>입&nbsp;&nbsp;&nbsp;&nbsp; 
          </label>
        </div>
        <div class="col radio-b">
          <button on:click={() => {video.conversation = none
                                  video.lesbian = none
                                  video.ani = none
                                  video.oral = none
                                }}>
          clear</button><br><br><br>
        </div>
    </div>

    
    <div class="row" style="font-size: smaller; padding:0;">
      <div class="col radio-c">
        <label>
          <input type="radio" name='masturbation' bind:group={video.masturbation} value={true}>자위 
        </label><br>
        <label class="text-danger font-weight-bold">
          <input type="radio" name='masturbation' bind:group={video.masturbation} value={false}>자위 
        </label>
      </div>
      <div class="col radio-c">
        <label style="font-size: smaller;">
          <input type="radio" name='massage' bind:group={video.massage} value={true}>마사지 
        </label><br>
        <label class="text-danger font-weight-bold" style="font-size: smaller;">
          <input type="radio" name='massage' bind:group={video.massage} value={false}>마사지 
        </label>
      </div>
      <div class="col radio-c">
        <label>
          <input type="radio" name='uniform' bind:group={video.uniform} value={true}>회사 
        </label><br>
        <label class="text-danger font-weight-bold">
          <input type="radio" name='uniform' bind:group={video.uniform} value={false}>회사 
        </label>
      </div>
      <div class="col radio-c">
        <label style="font-size: smaller;">
          <input type="radio" name='family' bind:group={video.family} value={true}>family 
        </label><br>
        <label class="text-danger font-weight-bold" style="font-size: smaller;">
          <input type="radio" name='family' bind:group={video.family} value={false}>family 
        </label>
      </div>
      <div class="col radio-b">
        <button on:click={() => {video.masturbation = none
                                  video.massage = none
                                  video.uniform = none
                                  video.family = none}}>
          clear</button>
        </div>
      </div>
      
      
      
      
      
      
      
      
      
      <br>
      <div class="row">
        <div class="col" style="display: inline-block;">
          <label style="font-size: smaller;">
            <input type="radio" name="ad_start" bind:group={video.ad_start} value="{true}"/>광고
          </label> 
          <label class="text-danger font-weight-bold" style="font-size: smaller;">
            <input type="radio" name="ad_start" bind:group={video.ad_start} value="{false}"/>광고
          </label>
          <button on:click={() => {video.ad_start = none}} style="font-size: smaller;">clear</button>
        </div>
        <div class="col" style="font-size: smaller;">
        별점 : 
        <select bind:value={video.star}>
          <option value={none}></option>
          <option value={null}>None</option>
          <option value={true}>all</option>
          <option value="1">♥</option>
          <option value="2">♥♥</option>
          <option value="3">♥♥♥</option>
          <option value="4">♥♥♥♥</option>
          <option value="5">♥♥♥♥♥</option>
        </select>
        <b class="text-danger">{"♥".repeat(video.star)}</b> 
      </div>
    </div>
    <br>
    <div style="display: flex; justify-content: flex-end; font-size: smaller;">
      <label>
        <input type="radio" name='vote' bind:group={video.vote} value={true}>vote &nbsp;
      </label>
      <button on:click={() => {video.vote = none}} style="font-size: smaller;">clear</button>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    </div>
  <br>
</div>

  <style>
    .header-button {
      display: flex;
      font-size: smaller;
      justify-content: space-around;
    }
    span {
      text-align: end;
    }
    .row {
      display: flex;
    }
    .radio-b {
      font-size: smaller; 
      margin: 0; 
    padding: 0;
  }
  .radio-c {
    /* display: flex; */
  }

  .button-group {
    /* display: inline-flex; */
    text-align: end;
    /* border: 1px solid #cccccc; */
    border-radius: 4px;
    /* overflow: hidden; */
    font-size: smaller;
  }
  
  .button {
    font-size: smaller;
    padding: 10px 16px;
    outline: none;
    border: none;
    cursor: pointer;
    border-right: 1px solid #ffffff;
    background: #ffffff;
    /* font-family: "Inter", sans-serif; */
  }
  
  .button:last-child {
    border-right: none;
  }
  
  .button:hover {
    background: #cccccc;
  }
  
  .page-item {
    font-size: smaller;
  }
  
  </style>