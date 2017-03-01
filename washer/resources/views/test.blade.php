@extends('app')

@section('htmlheader_title')
    工作状态查看
@endsection

@section('main-content')
    <div class="container">
        <div class="row">
            <div class="col-md-10 col-md-offset-1">
                <div class="panel panel-default">
                    <div class="panel-heading">Home</div>

                    <div class="panel-body">
                        @foreach($data as $d)
                            <p>Name {{$d->name}}}</p>
                            <p>Value {{$d->value}}</p>
                            <p>timestamp {{$d->timestamp}}</p>
                        @endforeach

                    </div>
                </div>
            </div>
        </div>
    </div>
@endsection
